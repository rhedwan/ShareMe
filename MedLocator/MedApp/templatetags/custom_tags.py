from django import template
from django.template.defaultfilters import register
from MedApp.models import StoreCategory


register = template.Library()

@register.simple_tag(name='categories')

def all_categories():
    return StoreCategory.objects.all()
    



