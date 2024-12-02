from django.urls import path
from rest_framework.routers import DefaultRouter

from NetworkManager.views import NetworkNodeViewSet
from NetworkManager.apps import NetworkmanagerConfig


app_name = NetworkmanagerConfig.name

router = DefaultRouter
router.register(r'network', NetworkNodeViewSet, basename='network')

urlpatterns = [

] + router.urls
