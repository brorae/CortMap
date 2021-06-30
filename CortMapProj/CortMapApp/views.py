from django.shortcuts import render, redirect
from .models import Rental
from .checking import *

import requests
# Create your views here.
def main(request):
    return render(request,'main.html')

def data(request):
    datas = response.json()
    context = {
        'data' : response,
        "json": getCountriesInformation(),
        "vacjson": getVaccineInformation(),
    }
    return render(request,'data.html',context)