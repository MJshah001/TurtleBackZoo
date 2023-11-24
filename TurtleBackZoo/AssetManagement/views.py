from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def asset_home(request):
    return render(request,'home.html',{'name':'asset_home'})