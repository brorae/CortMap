import requests

def getCountrylist():
    ret = []
    for ctry in datas:
        ret.append((ctry["country"],
                    ctry["countryInfo"]["iso2"],
                  ))
    return ret

def getCountryTodayCases(country):
    for ctry in datas:
        if ctry["country"] == country:
            return ctry["todayCases"]

def getCountryTodayDeaths(country):
    for ctry in datas:
        if ctry["country"] == country:
            return ctry["todayCases"]

def getCountriesInformation():
    ret = []
    for ctry in datas:
        ret.append((ctry["country"],
                    str(ctry["countryInfo"]["lat"]),
                    str(ctry["countryInfo"]["long"]),
                    ctry["countryInfo"]["flag"],
                    str(ctry["population"]),
                    str(ctry["cases"]),
                    str(ctry["todayCases"]),
                    str(ctry["deaths"]),
                    str(ctry["todayDeaths"]),
                    str(ctry["tests"]),
                  ))
    return ret

headers = {
            'accept': 'application/json',
          }

params =  (
          )

response = requests.get('https://disease.sh/v3/covid-19/countries', headers=headers, params=params)
datas = response.json()