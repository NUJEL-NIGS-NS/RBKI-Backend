from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('email','user_name','department', 'is_active', 'is_staff')
    search_fields = ('email', 'user_name')
    list_filter = ('is_active', 'is_staff')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email' ,'user_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',  'user_name','department', 'password1', 'password2'),
        }),
    )
    filter_horizontal = []

admin.site.register(User, CustomUserAdmin)
