from django.urls import path, include
from rest_framework.routers import DefaultRouter

from NetworkManager.views import NetworkNodeViewSet, ContactViewSet, ProductViewSet
from NetworkManager.apps import NetworkmanagerConfig


app_name = NetworkmanagerConfig.name

router = DefaultRouter()
router.register(r'network', NetworkNodeViewSet, basename='network')
router.register(r'contacts', ContactViewSet, basename='contacts')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    ]