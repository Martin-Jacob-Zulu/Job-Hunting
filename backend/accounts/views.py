from django.contrib.auth import login, authenticate, get_user_model
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView

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
                return Response({'success': 'Account created successfully'})
        else:
            return Response({'error': 'Passwords do not match'})
