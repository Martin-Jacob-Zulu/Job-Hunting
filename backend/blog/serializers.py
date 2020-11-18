from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = BlogPost
        fields = [ 'username', 'title', 'category', 'image', 'excerpt', 'content', 'date_updated', 'date_created',]
        lookup_field = 'slug'

    def get_username_from_author(self, blog_post):
        username = blog_post.author.username
        return username
