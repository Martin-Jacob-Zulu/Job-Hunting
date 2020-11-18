from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from accounts.models import UserAccount
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )


class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )


class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )


class BlogPostCategoryView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, formart=None):
        data = self.request.data
        category = data['category']
        queryset = BlogPost.objects.order_by(
            '-date_created').filter(category__iexact=category)

        serializer = BlogPostSerializer(queryset, many=True)

        return Response(serializer.data)


@api_view(['PUT', ])
def api_update_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = BlogPostSerializer(blog_post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "updated successfully"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)


@api_view(['DELETE', ])
def api_update_blog_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = blog_post.delete()
        data = {}
        if operation:
            data["success"] = "deleted successfully"
        else:
            data["failure"] = "request failed"
        return Response(data=data)


@api_view(['POST', ])
def api_create_blog_view(request):

    account = UserAccount.objects.get(pk=1)

    blog_post = BlogPost(author=account)

    if request.method == "POST":
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)

