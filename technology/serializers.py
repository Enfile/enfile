from rest_framework import serializers

from .models import Product, Experience


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
