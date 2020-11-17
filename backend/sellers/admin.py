from django.contrib import admin
from .models import Seller

class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'top_seller', 'trending_seller')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_filter = ('top_seller', 'trending_seller')
    list_per_page = 25

admin.site.register(Seller, SellerAdmin)
