from rest_framework import serializers

from NetworkManager.models import Product, Contact, NetworkNode
from NetworkManager.validators import ProviderValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    validators = [
        ProviderValidator(provider_field='provider', node_type_field='node_type'),
    ]
    class Meta:
        model = NetworkNode
        field = '__all__'
