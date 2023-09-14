from rest_framework import serializers

from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    """
    For serializing only selected fields of a Post
    """
    class Meta:
        model = Posts
        fields = ('id', 'created_by', 'title', 'created_on', 'total_votes')


class PostsSerializerAll(serializers.ModelSerializer):
    """
    For serializing all fields of a Post
    """
    class Meta:
        model = Posts
        fields = '__all__'
