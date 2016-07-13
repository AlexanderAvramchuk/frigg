# -*- coding: utf-8
from django.contrib import admin
from models import Feed, Video, Text, FeedType, Post, Like


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1


class TextInline(admin.TabularInline):
    model = Text
    extra = 1


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


class FeedAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    inlines = [VideoInline, TextInline, PostInline]

    class Meta:
        model = Feed


class VideoAdmin(admin.ModelAdmin):
    list_display = ('feed', 'video_url', )
    search_fields = ('feed__title', )

    class Meta:
        model = Video


class TextAdmin(admin.ModelAdmin):
    list_display = ('feed', )
    search_fields = ('feed__title', )

    class Meta:
        model = Text


class FeedTypeAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )

    class Meta:
        model = FeedType


class PostAdmin(admin.ModelAdmin):
    #list_display = ('feed', 'author', 'post_type')
    search_fields = ('feed__title', )
    #list_filter = ('post_type', )

    class Meta:
        model = Post


class LikeAdmin(admin.ModelAdmin):
    list_display = ('feed', 'user', )
    search_fields = ('user', )

    class Meta:
        model = Like


admin.site.register(Feed, FeedAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(FeedType, FeedTypeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
