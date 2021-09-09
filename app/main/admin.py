from django.contrib import admin

from main.models import Book, FavoriteBook

admin.site.register(Book)
admin.site.register(FavoriteBook)
