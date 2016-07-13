from models import Feed, Video, Text, FeedType, Post, Like
from rest_framework import serializers


class FeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feed
        fields = ('url', 'id', 'title', 'description', 'created_at',
                  'updated_at', 'video_url', 'text', 'type', 'author', )


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('url', 'id', 'title', 'description', 'created_at',
                  'updated_at', 'video_url', 'text', 'type', 'author',)


class TextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Text
        fields = ('url', 'id', 'title', 'description', 'created_at',
                  'updated_at', 'video_url', 'text', 'type', 'author',)


class FeedTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedType
        fields = ('url', 'id', 'title', )


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'description', 'created_at',
                  'updated_at', 'video_url', 'text', 'type', 'author',)


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = ('url', 'id', 'feed', 'user', 'created_at', )
