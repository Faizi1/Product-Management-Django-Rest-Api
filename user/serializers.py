from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import User


class UserSerializer(ModelSerializer):
    user_id = SerializerMethodField()
    def get_user_id(self, obj):
        if obj.id:
            return obj.id
    class Meta:
        model = User
        fields = ['user_id','username', 'email', 'password', 'first_name',
                  'last_name', 'is_active']