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
    level = serializers.SerializerMethodField()

    def get_level(self, obj):
        if obj.node_type == 'FC' or obj.provider is None:
            return 0
        elif obj.provider.node_type == 'FC':
            return 1
        else:
            return 2


    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt',)
