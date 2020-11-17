from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Seller
from .serializers import SellerSerializer


class SellerListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    pagination_class = None


class SellerView(RetrieveAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Seller.objects.filter(top_seller=True)
    serializer_class = SellerSerializer
    pagination_class = None
