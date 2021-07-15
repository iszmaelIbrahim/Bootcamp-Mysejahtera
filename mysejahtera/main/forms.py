from django import forms

from django.forms import fields
from .models import health, vaccine, location_qr
from main import models
# from .models import profile



class healthupdateform(forms.ModelForm):
    class Meta:
        model = health
        fields = [
            'fever',
            'Chills', 
            'headache', 
            'vomiting',
            'diarrhea',
            ] 


class vaccineform(forms.ModelForm):
    class Meta:
        model = vaccine
        fields = [
            'name',
            'age',
            'state',
            'date'
        ]

class qrcreateform(forms.ModelForm):
    class Meta:
        model = location_qr
        fields = [
            'name', 'address', 'city', 'state'
        ]
