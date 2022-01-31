import django_filters
from django_filters import DateFilter

from .models import *


class PropertyFilter(django_filters.FilterSet):
    propname = django_filters.CharFilter(
        field_name='name', lookup_expr='icontains')
    location = django_filters.CharFilter(
        field_name='location', lookup_expr='icontains')

    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['created', 'updated', 'location']


class UnitFilter(django_filters.FilterSet):
    class Meta:
        model = Unit
        fields = ['property', 'type', 'status']


class ProfileFilter(django_filters.FilterSet):
    suppname = django_filters.CharFilter(
        field_name='name', lookup_expr='icontains')
    # suppidno = django_filters.CharFilter(field_name='idno', lookup_expr='icontains')
    # suppphone = django_filters.CharFilter(field_name='phone', lookup_expr='icontains')

    class Meta:
        model = Profile
        fields = ['type']


class UnitOccupancyFilter(django_filters.FilterSet):
    class Meta:
        model = Unit_Occupancy
        fields = '__all__'
        exclude = ['created', 'updated']
