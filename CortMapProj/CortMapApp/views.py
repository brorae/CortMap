from django.shortcuts import render, redirect
from .models import Rental

import requests

# Create your views here.
def main(request):
    return render(request,'main.html')

def data(request):
    headers = {
        'accept': 'application/json',
    }

    params = (
        ('strict', 'true'),
    )

    response = requests.get('https://disease.sh/v3/covid-19/countries/KOR', headers=headers, params=params)

    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    # response = requests.get('https://disease.sh/v3/covid-19/countries/KOR?strict=true', headers=headers)
    context = {
        'data' : response,
        "json": response.text,
    }
    return render(request,'data.html',context)