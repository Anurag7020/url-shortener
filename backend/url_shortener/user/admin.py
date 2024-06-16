# In your application's admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel


class CustomUserAdmin(UserAdmin):
    model = UserModel
    list_display = ['email', 'name', 'username']
    # list_filter = ['is_active']  # Update list_filter here
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'username')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name' 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'username', 'name',)
    ordering = ('email',)


admin.site.register(UserModel, CustomUserAdmin)
