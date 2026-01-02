from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source="user.username", read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user_username', 'content', 'created_at', 'likes_count', 'media']
