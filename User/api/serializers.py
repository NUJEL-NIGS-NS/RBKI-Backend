from rest_framework import serializers
from ..models import User


class RegistrationSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    security =serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ["email", "user_name", "department", "password", "password2","security"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):
        user = User(
            email=self.validated_data["email"],
            department = self.validated_data['department'],
            user_name=  self.validated_data["user_name"],
        )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        security =self.validated_data["security"]
        
        if password != password2:
            raise serializers.ValidationError("Passwords Must Match")

        if int(security) != 12345:
            raise serializers.ValidationError({'security' : 'The security Id is wrong'})
            

        else:
            user.set_password(password)
            user.save()
            return user
