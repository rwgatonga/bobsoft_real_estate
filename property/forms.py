from django.forms import ModelForm
from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['type','created', 'updated']


class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'
        exclude = ['created', 'updated']


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['created', 'updated']


class UnitOccupancyForm(ModelForm):
    class Meta:
        model = Unit_Occupancy
        fields = '__all__'
        exclude = ['created', 'updated']
