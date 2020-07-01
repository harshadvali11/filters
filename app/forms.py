from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name=forms.CharField(max_length=25,validators=[validators.MaxLengthValidator(5)])
    num=forms.IntegerField(max_value=78,validators=[validators.MaxValueValidator(34)])
    phone=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])


    #validators=[validator1,validator2,..........]