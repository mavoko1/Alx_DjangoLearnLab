from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show in admin
    search_fields = ('title', 'author')                     # enable search
    list_filter = ('publication_year',)                     # filter by year
