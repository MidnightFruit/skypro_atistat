from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
import django_filters.rest_framework

from NetworkManager.models import Product, Contact, NetworkNode
from NetworkManager.serializers import NetworkNodeSerializer, ContactSerializer, ProductSerializer
from User.permissions import IsActive
from NetworkManager.filters import ContryFilter


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class  = ContryFilter

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsActive]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsActive]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsActive]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsActive]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsActive]

        return [permission() for permission in self.permission_classes]
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsActive]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsActive]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsActive]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsActive]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsActive]

        return [permission() for permission in self.permission_classes]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsActive]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsActive]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsActive]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsActive]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsActive]

        return [permission() for permission in self.permission_classes]
