from django.contrib import admin
from django.utils.translation import gettext_lazy as _
import django_filters

from NetworkManager.models import Contact, NetworkNode


class CityFilter(admin.SimpleListFilter):
    title = 'Фильтрация по городу'
    parameter_name = 'contacts_city'

    def lookups(self, request, model_admin):
        contacts = Contact.objects.all()
        return [(contact.id, contact.city) for contact in contacts]
    
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contact__id=self.value())
        return queryset
    

class ContryFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='contacts__country', lookup_expr='icontains')
    class Meta:
        model = NetworkNode
        fields = ['country']