from rest_framework import serializers
from .models import NewsModel


class NewsModelSerializer(serializers.ModelSerializer):
    news_id = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = NewsModel
        fields = '__all__'
