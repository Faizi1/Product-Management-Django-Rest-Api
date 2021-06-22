from django.urls import path
from .views import UserSignUpView, UserSignInView


urlpatterns = [

    # User SignUp, Login url
    path('signup/',UserSignUpView.as_view({'post': 'create','get':'list'}),
                                         name='user_url'),
    path('signup/<int:user_id>/',UserSignUpView.as_view({'get': 'get_user_detail'}),
                                         name='user_url'),
    path('signup/<int:user_id>/',UserSignUpView.as_view({'delete': 'delete'}),
                                         name='user_url'),

    path('login/', UserSignInView.as_view(), name = "signin"),
]