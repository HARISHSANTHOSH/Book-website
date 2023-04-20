from django import forms
from django.contrib.auth.models import User
from .models import *



class userregisterform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class userloginform(forms.Form):
    username=forms.CharField(max_length=40)
    password=forms.CharField(max_length=40)

class bookform(forms.ModelForm):
    class Meta :
        model =bookmodel
        fields = '__all__'