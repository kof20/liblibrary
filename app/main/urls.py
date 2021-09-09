from django.urls import path, include
from django.views.generic import TemplateView

from main import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path("register/", views.RegisterUserView.as_view(), name="register"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('book/', views.BookListView.as_view(), name='book'),
    path('favorite/', views.FavoriteListView.as_view(), name='favorite'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('', TemplateView.as_view(template_name="main/index.html")),
    path('addfavorite/<int:pk>', views.AddToFavoriteView.as_view(), name='addfavorite'),
    path('deletefavorite/<int:pk>', views.DeleteFromFavoriteView.as_view(), name='deletefavorite'),
    path('isread/<int:pk>', views.AddToIsRead.as_view(), name='isread'),

]
