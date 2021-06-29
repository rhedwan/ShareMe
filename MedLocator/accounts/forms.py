from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import  User
from django import forms
from django.db import models
from django.forms import fields


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    accept_terms = forms.BooleanField(widget=forms.CheckboxInput())
    phome_number =  forms.CharField(max_length=100 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields +('username', 'first_name', 'last_name', 'email', 'password1','password2', 'accept_terms','phome_number')