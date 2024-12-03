from rest_framework import serializers


class ProviderValidator:
    def __init__(self, provider_field, node_type_field):
        self.provider_field = provider_field
        self.node_type_field = node_type_field
    

    def __call__(self, data, *args, **kwds):
        self.validate_factory_provider(data)
    

    def validate_factory_provider(self, data):
        provider = data.get(self.provider_field)
        node_type = data.get(self.node_type_field)
        
        if node_type == 'FC' and provider is not None:
            raise serializers.ValidationError('У завода не может быть поставщика')
