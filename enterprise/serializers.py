from rest_framework import serializers

from .models import Employer, About


class HomeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Employer
        fields = '__all__'


class MyVacancySerializer(serializers.ModelSerializer):
    company = HomeSerializer(read_only=True)

    class Meta:
        model = About
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    #ccc = serializers.SlugRelatedField(read_only=True, slug_field='company')
    class Meta:
        model = About
        fields = '__all__'