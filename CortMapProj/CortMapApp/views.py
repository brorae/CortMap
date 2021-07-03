from django.shortcuts import render, redirect, get_object_or_404
from .datas import *
from .models import Blog, Blogg

import requests
# Create your views here.


def main(request):
    datas = response.json()
    context = {
        "CorData": getCountriesInformation(),
    }
    return render(request, 'main2.html', context)


def data(request):
    datas = response.json()
    context = {
        "CorData": getCountriesInformation(),
        "CorData2": getProhibitionInformation(),
        "CorData3": getPossibleTravel(),
        "CorData4": getImpossibleTravel(),
    }
    return render(request, 'data.html', context)


def base(request):
    return render(request, 'index.html')


def showProhibition(request):
    datas = response.json()
    context = {
        "CorData": getCountriesInformation(),
        "ProhibitCorData": getProhibitionInformation(),
    }
    return render(request, 'showProhibition.html', context)


def recommend(request):
    blogs = Blog.objects.all()
    bloggs = Blogg.objects.all()
    context = {
        'blogs': blogs,
        'bloggs': bloggs
    }
    return render(request, 'recommend.html', context)


def detail(request, id):
    detail_data = get_object_or_404(Blog, pk=id)
    context = {
        'title': detail_data.title,
        'body': detail_data.body,
        'image': detail_data.image,
    }
    return render(request, 'detail.html', context)

def travelPossible(request):
    datas = response.json()
    context = {
        "CorData": getCountriesInformation(),
        "TravelPossibleCountry" : getPossibleTravel(),
        "TravelImpossibleCountry" : getImpossibleTravel(),
    }
    return render(request,'travelPossible.html',context)

