from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age',)
    list_display_links = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name',)

admin.site.register(User, UserAdmin)