from django.shortcuts import render, redirect
from .datas import *

import requests
# Create your views here.
def main(request):
    return render(request,'main.html')

def data(request):
    datas = response.json()
    context = {
        "CorData": getCountriesInformation(),
    }
    return render(request,'data.html',context)