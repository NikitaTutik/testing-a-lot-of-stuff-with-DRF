from rest_framework import serializers
from .models import Posts, PostRates


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'post_title', 'post_body', 'rates')
        depth = 1


class PostRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRates
        fields = ('id', 'likes', 'dislikes')
