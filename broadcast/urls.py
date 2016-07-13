from rest_framework import routers
from views import *
from django.conf.urls import url


broadcast_router = routers.DefaultRouter()
broadcast_router.register(r'feeds', FeedViewSet)
broadcast_router.register(r'videos', VideoViewSet)
broadcast_router.register(r'texts', TextViewSet)
broadcast_router.register(r'feed_types', FeedTypeViewSet)
broadcast_router.register(r'posts', PostViewSet)
broadcast_router.register(r'likes', LikeViewSet)