from rest_framework import serializers

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


class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(required=False)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(**profile_data)
        user = User.objects.create(profile=profile, **validated_data)
        return user
        
    class Meta:
        model = User
        fields = ('user_id','profile','is_active','created_at','updated_at')

     
