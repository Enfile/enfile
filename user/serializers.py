from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django_filters import rest_framework as filters

from technology.serializers import ExperienceSerializer, ProductSerializer, TechnologySerializer
from .models import Account, Profile, User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'sub',
            'created_at',
            'updated_at',
        )


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
    account = AccountSerializer()
    profile = ProfileSerializer(required=False)
    experiences = ExperienceSerializer(required=False, many=True)
    products = ProductSerializer(required=False, many=True)
    technologies = TechnologySerializer(required=False, many=True)

    class Meta:
        model = User
        fields = (
            'user_id',
            'account',
            'profile',
            'experiences',
            'products',
            'technologies',
            'is_active',
            'created_at',
            'updated_at',
        )


class UserFilter(filters.FilterSet):
    account__sub = filters.CharFilter(lookup_expr='exact')
    profile__name = filters.CharFilter(lookup_expr='contains')
    profile__school_name = filters.CharFilter(lookup_expr='contains')
    profile__using_os = filters.CharFilter(lookup_expr='contains')
    technologies__name = filters.CharFilter(lookup_expr='exact')

    order_by = filters.OrderingFilter(
        fields=(
            ('technologies__technology_level_id', 'order_by_level'),
        ),
    )

    class Meta:
        model = User
        fields = (
            'account__sub',
            'profile__name',
            'profile__school_name',
            'profile__using_os',
            'technologies__name',
        )
