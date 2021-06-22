"""
Business Logic for the user app
"""

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

class UserController():
    def create_user(self, payload_data):
        """[Create a user]

        Args:
            payload_data ([dict]): [attr dict request made by client]
        """
        try:
            # hashed from plain text
            if not 'password' in payload_data:
                return Response({'Error': True, 'Message':'Password is required','Status': 400,'data':[]})
            payload_data['password'] = make_password(payload_data['password'])

            serialized = UserSerializer(data=payload_data)

            if serialized.is_valid(raise_exception=True):

                # Rollback db transaction if exception is thrown
                with transaction.atomic():
                    user = serialized.save()
                    serialized_user = UserSerializer(user)
                    print(serialized_user)
                return Response({'Error': False, 'Message':'User Created!!','Status': 200,'data':serialized_user.data})
        except Exception as e:
            print(e)
            return Response({'Error': True, 'Message':'UnSuccessfull','Status': 500,'data':[str(e)]})

    def get_user(self,request):
        try:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response({'Error':False, 'Message':'All Users!','Status':200,'data':serializer.data})
        except Exception as e:
            print(e)
            return Response({'Error':True,'Message':'Unseccessull','Status':500,'data':[str(e)]})

    def get_detail_user(self,user_id):
        """ Get User via id """
        try:
            user = User.objects.get(pk=user_id)
            serializer = UserSerializer(user)
            return Response({'Error':False,'Message':'Successull','Status':200,'data':serializer.data})
        except ObjectDoesNotExist as e:
            print(e)
            return Response({'Error':True,'Message':'Not Found','Status':500,'data':[str(e)]})
        except Exception as e:
            print(e)
            return Response({'Error':True,'Message':'UnSuccessull','Status':500,'data':[str(e)]})

    def delete_user(self,user_id):
        """ Delete User """
        try:
            user = User.objects.get(pk=user_id)
            user.delete()
            return Response({'Error':False, 'Message':"User Deleted!!",'Status':200, 'data':[]})
        except ObjectDoesNotExist as e:
            return Response({'Error':True, 'Message':'Not Found!', 'Status':500, 'data':[str(e)]})
        except Exception as e:
            return Response({'Error':True, 'Message':'Unseccessul','Status':500, 'data':[str(e)]})