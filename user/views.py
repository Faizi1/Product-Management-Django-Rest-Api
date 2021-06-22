"""
API for user

UserSignUpView
UserSignInView
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


from .models import User
from .serializers import UserSerializer
from .usercontroller import UserController

user_controller = UserController()

class UserSignUpView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """CREATE a User/Signup"""

        result = user_controller.create_user(request.data)
        return result

    def list(self, request, *args,  **kwargs):
        """Get list of Users"""
        result = user_controller.get_user(request.data)
        return result

    def get_user_detail(self,request, user_id):
        """ Get user via  userid"""
        result = user_controller.get_detail_user(user_id)
        return result

    def delete(self, request, user_id):
        """ Delete user """
        result = user_controller.delete_user(user_id)
        return result
class UserSignInView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        """ SignIn User """
        try:
            serializer = self.serializer_class(data= request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'Token': token.key})
        except Exception as e:
            print(e)
            return Response({'Error':True, 'Message':'Unsuccessull', 'status':500, 'data': [str(e)]})