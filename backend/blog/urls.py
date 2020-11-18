from django.urls import path
from .views import (
        BlogPostCategoryView, 
        BlogPostDetailView, 
        BlogPostFeaturedView, 
        BlogPostListView,
        api_update_blog_view,
        api_create_blog_view,
    )

urlpatterns = [
    path('', BlogPostListView.as_view()),
    path('featured', BlogPostFeaturedView.as_view()),
    path('category', BlogPostCategoryView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),
    path('<slug>', api_update_blog_view),
    path('<slug>', api_create_blog_view),
]
