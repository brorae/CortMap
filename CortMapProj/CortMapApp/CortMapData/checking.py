import requests

def getCountrylist():
    ret = []
    for ctry in datas:
        ret.append((ctry["country"], ctry["countryInfo"]["iso2"]))
    return ret

def getCountryTodayCases(country)




headers = {
           'accept': 'application/json',
          }

params =  (
          )

response = requests.get('https://disease.sh/v3/covid-19/countries', headers=headers, params=params)
datas = response.json()
for country in datas:
    print(country["country"], country["countryInfo"]["iso2"],sep = ",")