from django import forms
from django.forms import widgets
from .models import StoreItem 





class StoreItemForm(forms.ModelForm):
    class Meta:
        model =  StoreItem 
        fields = ['name','price','store_owner','description','image','category']

        widgets = {
            # 'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'} )
        }

