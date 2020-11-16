from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView