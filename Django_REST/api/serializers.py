from rest_framework import serializers
# import django.contrib.auth.password_validation as validators
from . import models

# class FriendSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Friend
#         fields = ('id', 'name')

# class BelongingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Belonging
#         fields = ('id', 'name')

# class BorrowedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Borrowed
#         fields = ('id', 'what', 'to_who', 'when', 'returned')

class RegistrationSerializer(serializers.ModelSerializer):

    # password2 = serializers.CharField(style={'input_type': 'password2'}, write_only=True)

    class Meta:
        model = models.User
        fields = ('id','username', 'password')
