from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Applicant, User, Follow


class HomeHhSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Applicant
        fields = '__all__'



class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]
