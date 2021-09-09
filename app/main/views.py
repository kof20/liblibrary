from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from .forms import RegisterUserForm, LoginUserForm
from main.models import Book, FavoriteBook


class BookListView(ListView):
    model = Book
    template_name = 'main/books.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'main/book.html'
    context_object_name = 'book'


class FavoriteListView(View):

    def get(self, request, *args, **kwargs):
        favorite_books = FavoriteBook.objects.filter(user=request.user)
        context = {
            'fav': favorite_books,
        }
        return render(request, 'main/favorite.html', context)


class AddToFavoriteView(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        book_id = kwargs.get('pk')
        if FavoriteBook.objects.filter(book=book_id, user=user_id):
            return HttpResponseRedirect(reverse_lazy('favorite'))
        else:
            FavoriteBook.objects.create(
                user_id=user_id, book_id=book_id
            )
        return HttpResponseRedirect(reverse_lazy('favorite'))


class AddToIsRead(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        book_id = kwargs.get('pk')
        favorite = FavoriteBook.objects.get(book=book_id, user=user_id)
        if favorite.is_read:
            return HttpResponseRedirect(reverse_lazy('favorite'))
        else:
            favorite.is_read = True
            favorite.save()
        return HttpResponseRedirect(reverse_lazy('favorite'))


class DeleteFromFavoriteView(View):
    def get(self, request, *args, **kwargs):
        user = request.user.id
        book = kwargs.get('pk')
        x = Book.objects.get(id=book)
        favorite = FavoriteBook.objects.filter(user_id=user, book_id=book)
        if favorite:
            instance = favorite
            instance.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class RegisterUserView(CreateView):
    model = User
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('book')


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('book')

    def get_success_url(self):
        return self.success_url


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('book')
