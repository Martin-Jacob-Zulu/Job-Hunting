from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'is_active', 'is_admin', 'last_login', 'date_joined', 'is_staff')
    list_display_links = ('name', 'username')
    search_fields = ('name', 'username', 'is_active')
    list_filter = ('date_joined', 'is_active', 'is_staff')
    list_editable = ('is_admin', 'is_staff')
    readonly_fields = ('username', 'email', 'password')


admin.site.register(Account, AccountAdmin)
