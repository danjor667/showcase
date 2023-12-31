from rest_framework.serializers import ModelSerializer
from .models import Profile
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'project_set', 'profile_set']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        profile = Profile.objects.create_profile(User=user, email=user.email)
        return user, profile



class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'