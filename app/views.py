from django.shortcuts import render

import datetime
# Create your views here.
from app import forms

def form(request):
    form=forms.ContactForm()
    if request.method=='POST':
        form_data=forms.ContactForm(request.POST)
        if form_data.is_valid():
            name=form_data.cleaned_data.get('name')
            num=form_data.cleaned_data.get('num')
            phone=form_data.cleaned_data.get('phone')
            d={'name':name,'num':num,'phone':phone}
            return render(request,'form_data.html',context=d)

    return render(request,'form.html',context={'form':form})

def filter(request):
    data=datetime.datetime.now()
    d={'wish':'hai hello how r u','data':data,'count':11,'name':'Python'}

    return render(request,'filter.html',context=d)