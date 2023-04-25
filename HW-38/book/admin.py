from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'price',)
    list_display_links = ('id', 'title', 'author',)
    search_fields = ('title', 'author',)

admin.site.register(Book, BookAdmin)