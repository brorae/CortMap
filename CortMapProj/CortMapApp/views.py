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
    return render(request, 'main.html', context)


def data(request):
    datas = response.json()
    context = {
        "CorData": getCountriesInformation(),
    }
    return render(request, 'data.html', context)


def base(request):
    return render(request, 'index.html')


def recommend(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    bloggs = Blogg.objects.all()
    contextt = {
        'bloggs': bloggs
    }
    return render(request, 'recommend.html', context, contextt)


def detail(request, id):
    detail_data = get_object_or_404(Blog, pk=id)
    context = {
        'title': detail_data.title,
        'body': detail_data.body,
        'image': detail_data.image,
    }
    return render(request, 'detail.html', context)
