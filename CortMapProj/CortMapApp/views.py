from django.shortcuts import render, redirect
from .datas import *

import requests
# Create your views here.
def main(request):
    datas = response.json()
    context = {
        "CorData": getCountriesInformation(),
    }
    return render(request,'main2.html',context)

def data(request):
    datas = response.json()
    context = {
        "CorData": getCountriesInformation(),
        "CorData2": getProhibitionInformation(),
        "CorData3": getPossibleTravel(),
        "CorData4": getImpossibleTravel(),
    }
    return render(request,'data.html',context)

def base(request):
    return render(request,'index.html')

def showProhibition(request):
    datas = response.json()
    context = {
        "CorData": getCountriesInformation(),
        "ProhibitCorData" : getProhibitionInformation(),
    }
    return render(request,'showProhibition.html',context)

def travelPossible(request):
    datas = response.json()
    context = {
        "CorData": getCountriesInformation(),
        "TravelPossibleCountry" : getPossibleTravel(),
        "TravelImpossibleCountry" : getImpossibleTravel(),
    }
    return render(request,'travelPossible.html',context)