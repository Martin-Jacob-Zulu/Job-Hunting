from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost


class BlogPostlAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'category', 'date_created', 'featured', 'trending')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'category')
    list_editable = ('featured', 'trending')
    list_per_page = 25
    summernote_fields = ('content',)


admin.site.register(BlogPost, BlogPostlAdmin)
