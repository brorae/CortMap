from django.shortcuts import render, redirect
from .datas import *

import requests
# Create your views here.
def main(request):
    datas = response.json()
    context = {
        "CorData": getCountriesInformation(),
    }
    return render(request,'main.html',context)

def data(request):
    datas = response.json()
    context = {
        "CorData": getCountriesInformation(),
    }
    return render(request,'data.html',context)