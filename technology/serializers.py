from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


from .models import Product, Experience, TechnologyLevel, Technology


class TechnologyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyLevel
        fields = [
            'level',
            'text',
            'created_at',
            'updated_at',
        ]


class TechnologySerializer(WritableNestedModelSerializer):
    technologyLevel = TechnologyLevelSerializer

    class Meta:
        model = Technology
        fields = [
            'technology_id',
            'technology_level',
            'name',
            'created_at',
            'updated_at',
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'product_id',
            'product_type',
            'link',
            'technology',
            'text',
            'created_at',
            'updated_at',
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'experience_id',
            'experience_type',
            'link',
            'technology',
            'text',
            'created_at',
            'updated_at'
        ]
