from rest_framework import serializers

from .models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'experience_id',
            'user',
            'experience_type',
            'link',
            'technology',
            'text',
            'create_at',
            'update_at'
        ]


