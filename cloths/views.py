from django.shortcuts import render
from .models import Cloth
from  .forms import ClothForm
from django.http import HttpResponseRedirect
# Create your views here.

def show(r):
    form =ClothForm()
    if r.method=='POST':
        form=ClothForm(r.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('')
    return render(r,'cloths/cloth.html',{'form':form})

def view(r):
    form=Cloth.objects.all()
    return render(r,'cloths/clothview.html',{'form':form})
