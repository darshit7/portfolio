import json

from django.contrib.auth import authenticate, login, logout

from rest_framework import status, views, permissions
from rest_framework.response import Response

from user_management.serializers import UserSerializer


class LoginView(views.APIView):
    '''
    '''

    def post(self, request, format=None):
        '''
        '''
        data = json.loads(request.body.decode('utf-8'))

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                serialized = UserSerializer(user)
                return Response(serialized.data)
            else:
                return Response({'status':'Unauthorized',
                    'message':'Username/Password combination is not valid.'},
                    status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'status':'Nouser',
                'message':'Username/Password combination is not valid.'},
                status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
    '''
    '''
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
