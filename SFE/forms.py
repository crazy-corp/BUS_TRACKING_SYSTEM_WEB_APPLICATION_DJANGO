from django import forms
from django.forms import widgets
from .models import sfed




class addbusform(forms.ModelForm):
    class Meta:
        model =sfed
        fields = ('Bus_ID','BusName',"Sce")

        widgets={
            'Bus_ID':forms.TextInput(attrs={'class':'form-control'}),
            'BusName':forms.TextInput(attrs={'class':'form-control'}),
            'Sce': forms.TextInput(),
            }
        