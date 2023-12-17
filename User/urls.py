from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegistration,delete_token,user_details,reset_password
urlpatterns = [
    path('login',obtain_auth_token, name='token_obtain_pair'),
    path('register',UserRegistration,name='User Registration'),
    path('logout',delete_token,name='User Logout and token delete'),
    path('user',user_details,name='User details'),
    path('passRes',reset_password,name='Reset password'),


]
