from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from technology.serializers import ExperienceSerializer, ProductSerializer, TechnologySerializer
from .models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'profile_id',
            'icon_path',
            'name',
            'sex',
            'birth_day',
            'school_year',
            'school_name',
            'profile',
            'using_os',
            'link',
            'contact',
            'created_at',
            'updated_at'
        )


class UserSerializer(WritableNestedModelSerializer):
    profile = ProfileSerializer(required=False)
    experiences = ExperienceSerializer(many=True)
    products = ProductSerializer(many=True)
    technologies = TechnologySerializer(many=True)

    class Meta:
        model = User
        fields = (
            'user_id',
            'profile',
            'experiences',
            'products',
            'technologies',
            'is_active',
            'created_at',
            'updated_at',
        )
