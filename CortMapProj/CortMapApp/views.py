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

    '''
    {
    "updated": 1624965947861,
    "country": "S. Korea",
    "countryInfo": {
        "_id": 410,
        "iso2": "KR",
        "iso3": "KOR",
        "lat": 37,
        "long": 127.5,
        "flag": "https://disease.sh/assets/img/flags/kr.png"
    },
    "cases": 156167,
    "todayCases": 595,
    "deaths": 2017,
    "todayDeaths": 2,
    "recovered": 147077,
    "todayRecovered": 402,
    "active": 7073,
    "critical": 152,
    "casesPerOneMillion": 3043,
    "deathsPerOneMillion": 39,
    "tests": 10555741,
    "testsPerOneMillion": 205713,
    "population": 51312904,
    "continent": "Asia",
    "oneCasePerPeople": 329,
    "oneDeathPerPeople": 25440,
    "oneTestPerPeople": 5,
    "undefined": 138,
    "activePerOneMillion": 137.84,
    "recoveredPerOneMillion": 2866.28,
    "criticalPerOneMillion": 2.96
    }
    '''
    datas = response.json()
    context = {
        'data' : response,
        "json": response.text,
        "jsontxt" : datas["cases"]
    }
    return render(request,'data.html',context)