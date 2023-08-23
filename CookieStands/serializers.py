from rest_framework import serializers
from .models import CookieStand


class CookieStandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookieStand
        # fields = '__all__'
        fields =['owner', 'title', 'desc']
