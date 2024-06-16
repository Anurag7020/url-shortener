from rest_framework import serializers
from .models import ShortenedURL, URLHit


class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['id', 'user', 'original_url', 'short_code', 'created_at']


class URLHitSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLHit
        fields = ['id', 'url', 'timestamp', 'ip_address', 'user_agent']
