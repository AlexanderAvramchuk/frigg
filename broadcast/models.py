# -*- coding: utf-8
from __future__ import unicode_literals
from django.db import models
from account.models import CustomUser as User
from ckeditor.fields import RichTextField


class FeedType(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "тип контента"
        verbose_name_plural = "Типы контента"


class Feed(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    users = models.ManyToManyField(User,
                                   through='Like',
                                   through_fields=('feed', 'user'),
                                   blank=True,
                                   related_name='voted_users')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    feed_type = models.ForeignKey(FeedType, related_name='feeds')

    @property
    def video_url(self):
        return self.video.video_url

    @property
    def text(self):
        return self.text.text

    @property
    def author(self):
        return self.post.author

    class Meta:
        verbose_name = "контент"
        verbose_name_plural = "Контент"

    @property
    def type(self):
        return self.feed_type.title

    def __unicode__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes')
    feed = models.ForeignKey(Feed, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return "user_id:%i, feed_id:%i" % (self.user.id, self.feed.id)

    class Meta:
        verbose_name = "лайк"
        verbose_name_plural = "Лайки"


class Video(models.Model):
    feed = models.OneToOneField(Feed, related_name='video')
    video_url = models.URLField()

    @property
    def title(self):
        return self.feed.title

    @property
    def description(self):
        return self.feed.description

    @property
    def created_at(self):
        return self.feed.created_at

    @property
    def updated_at(self):
        return self.feed.updated_at

    @property
    def type(self):
        return self.feed.feed_type.title

    def __unicode__(self):
        return self.feed.title

    class Meta:
        verbose_name = "видео урок"
        verbose_name_plural = "Видео уроки"


class Text(models.Model):
    feed = models.OneToOneField(Feed, related_name='text')
    text = RichTextField(blank=True)

    @property
    def title(self):
        return self.feed.title

    @property
    def description(self):
        return self.feed.description

    @property
    def created_at(self):
        return self.feed.created_at

    @property
    def updated_at(self):
        return self.feed.updated_at

    @property
    def type(self):
        return self.feed.feed_type.title

    def __unicode__(self):
        return self.feed.title

    class Meta:
        verbose_name = "текстовый урок"
        verbose_name_plural = "Текстовые уроки"


class Post(models.Model):
    feed = models.OneToOneField(Feed, related_name='post')
    author = models.ForeignKey(User, related_name='posts')

    @property
    def title(self):
        return self.feed.title

    @property
    def description(self):
        return self.feed.description

    @property
    def created_at(self):
        return self.feed.created_at

    @property
    def updated_at(self):
        return self.feed.updated_at

    @property
    def type(self):
        return self.feed.feed_type.title

    def __unicode__(self):
        return self.feed.title

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "Посты"
