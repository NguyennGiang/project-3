from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework import serializers

from module.account.models import User
from utils.format_service import FormatService


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ()

    def to_internal_value(self, data):
        if "phone_number" in data:
            phone_number = data.get("phone_number")
            phone_number = FormatService.phone_to_canonical_format(phone_number)
            if not phone_number:
                phone_number = None
            data["phone_number"] = phone_number
        if "email" in data:
            email = data.get("email").lower()
            data["username"] = email
            data["email"] = email
        if "password" in data:
            data["password"] = make_password(data.get("password"))
        return super().to_internal_value(data)

    def validate(self, data):
        if not ("email" in data or "phone_number" in data):
            raise serializers.ValidationError("Email or phone number is required")

        existed_user = User.objects.filter(
            Q(email=data.get("email", "")) | Q(phone_number=data.get("phone_number", ''))).first()
        if existed_user:
            raise serializers.ValidationError("Email already exists")
        return data


class ObtainTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if not ("email" in data or "phone_number" in data):
            raise serializers.ValidationError("Email or phone number is required")
        return data
