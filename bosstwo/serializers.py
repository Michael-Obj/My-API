from rest_framework.serializers import ModelSerializer
from bosstwo.models import StaffTwo
from django.contrib.auth.models import User
# from rest_framework import serializers

# class StaffSerializer(serializers.ModelSerializer):

class StaffSerializer(ModelSerializer):

    class Meta:
        model = StaffTwo
        exclude = ["age", "level"]
        # fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email"]