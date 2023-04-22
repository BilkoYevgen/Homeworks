from django.contrib import admin
from .models import Purchase

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('date', 'user_first_name', 'book_title',)
    list_display_links = ('book_title', 'user_first_name',)
    search_fields = ('book__title', 'user__first_name',)

    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = 'Імʼя користувача'

    def book_title(self, obj):
        return obj.book.title
    book_title.short_description = 'Назва книги'

admin.site.register(Purchase, PurchaseAdmin)
