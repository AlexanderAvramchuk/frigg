from rest_framework import routers
from views import UserViewSet
from django.conf.urls import url
from views import registration


account_router = routers.DefaultRouter()
account_router.register(r'users', UserViewSet)
urlpatterns = [
    url(r'^registration', registration),
]