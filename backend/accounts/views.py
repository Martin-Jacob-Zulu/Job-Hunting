from django.contrib.auth import login, authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import AccountPropertiesSerializer
from .models import UserAccount

User = get_user_model()


class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        username = data['username']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': "Email already in use."})
            elif User.objects.filter(username=username).exists():
                return Response({'error': "Username is not available"})
            else:
                if len(password) < 6:
                    return Response({'error': 'Password must be at least 6 characters long'})
                user = User.objects.create_user(email=email, username=username, password=password,
                                                name=name)
                user.save()
                data['success'] = 'Account created successfully'
                token = Token.objects.get(user=user).key
                data['token'] = token
                return Response(data)
        else:
            return Response({'error': 'Passwords do not match'})


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def account_properties_view(request):
    try:
        account = request.user
    except UserAccount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AccountPropertiesSerializer(account)
        return Response(serializer.data)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def account_update_view(request):
    try:
        account = request.user
    except UserAccount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = AccountPropertiesSerializer(account, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Account updated successfully"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)