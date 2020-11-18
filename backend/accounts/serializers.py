from rest_framework import serializers
from .models import UserAccount


class AccountPropertiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ['pk', 'email', 'username', 'name', ]