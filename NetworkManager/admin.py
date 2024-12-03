from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse_lazy

from NetworkManager.models import NetworkNode, Contact, Product
from NetworkManager.filters import CityFilter
from NetworkManager.serializers import NetworkNodeSerializer


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_link', 'product_link', 'provider_link', 'node_type', 'debt', 'level_field_display')
    list_filter = (CityFilter,)
    actions = ['clear_debts']

    def clear_debts(self, request, queryset):
        queryset.update(debt=0)

    def provider_link(self, obj):
        if obj.provider:
            url = reverse_lazy('admin:NetworkManager_networknode_change', args=[obj.provider.id])
            return format_html('<a href="{}">{}</a>', url, obj.provider.name)
        return "Нет поставщика"

    provider_link.short_description = 'Поставщик'
    provider_link.admin_order_field = 'provider__name'

    def product_link(self, obj):
        if obj.product:
            url = reverse_lazy('admin:NetworkManager_product_change', args=[obj.product.id])
            return format_html('<a href="{}">{}</a>', url, obj.product.name)
        return "Нет продукта"

    product_link.short_description = 'Продукт'
    product_link.admin_order_field = 'product__name'

    def contact_link(self, obj):
        if obj.contacts:
            url = reverse_lazy('admin:NetworkManager_contact_change', args=[obj.contacts.id])
            return format_html('<a href="{}">{}</a>', url, obj.contacts.email)
        return "Нет продукта"

    contact_link.short_description = 'Контакты'
    contact_link.admin_order_field = 'contacts__name'

    def level_field_display(self, obj):
        serializer = NetworkNodeSerializer(obj)
        return serializer.data['level']

admin.site.register(Contact)
admin.site.register(Product)
