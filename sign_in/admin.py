from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin (admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'profile', 'date_joined')
    list_filter = ('profile', 'date_joined')
    search_fields = ('first_name', 'last_name', 'username',
                     'email', 'mobile', 'date_joined')
