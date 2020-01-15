from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django_filters import rest_framework as filters


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


class UserFilter(filters.FilterSet):
    profile__name = filters.CharFilter(lookup_expr='contains')
    profile__school_name = filters.CharFilter(lookup_expr='contains')
    profile__using_os = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = User
        fields = (
            'profile__name',
            'profile__school_name',
            'profile__using_os',
        )
