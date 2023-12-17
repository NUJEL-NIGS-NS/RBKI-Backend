from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from .api.serializers import RegistrationSerializers


@api_view(["POST"])
def UserRegistration(request):
    serializer = RegistrationSerializers(data=request.data)

    data = {}
    if serializer.is_valid():
        User = serializer.save()
        data["Message"] = "User has been registered with email " + User.email
        token = Token.objects.get(user=User).key
        data["token"] = token
    else:
        data["Error"] = serializer.errors
    return Response(data)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_token(request):
    print(request.auth)
    data = {}
    try:
        user = Token.objects.get(user=request.user)
        user.delete()
        data["status"] = True
    except:
        data["status"] = False
    return Response(data)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_details(request):
    data = {}
    user = request.user
    try:
        data["username"] = user.user_name
        data["department"] = user.department

    except:
        pass
    return Response(data)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def reset_password(request):
    user = request.user
    data = {}
    try:
        if request.data["Security"] == "123456":
            new_password = request.data["password"]
            user.set_password(new_password)
            user.save()
            data["status"] = "Your password has been sucessfully changed"

    except:
        data["status"] = "Error Occured try after some time"
    return Response(data)
