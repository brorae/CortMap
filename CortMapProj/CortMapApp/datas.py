import requests

def getCountrylist():
    ret = []
    for ctry in datas:
        ret.append((ctry["country"],
                    ctry["countryInfo"]["iso2"],
                  ))
    return ret

def getCountriesInformation():
    ret = []
    for ctry in datas:
        i = 0
        origini = i
        isVac = True
        while (vacdatas[i]["country"] != ctry["country"]):
            i += 1
            if (i >= len(vacdatas)):
                i = origini
                isVac = False
                break
        if (isVac):
            ret.append((ctry["country"],                                 # 국가이름
                        str(ctry["countryInfo"]["lat"]),                 # 위도
                        str(ctry["countryInfo"]["long"]),                # 경도
                        ctry["countryInfo"]["flag"],                     # 국기 이미지 url
                        str(ctry["population"]),                         # 총 인구수
                        str(ctry["cases"]),                              # 총 확진자수
                        str(ctry["todayCases"]),                         # 금일 확진자수
                        str(ctry["deaths"]),                             # 총 사망자수
                        str(ctry["todayDeaths"]),                        # 금일 사망자수
                        str(ctry["tests"]),                              # 검사시행 인구수
                        str(vacdatas[i]["timeline"]["7/3/21"])          # 백신접종 인구수
                    ))
            i += 1
        else:
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
                        "백신정보 없음"
                    ))
    return ret

def getVaccineInformation():
    ret = []
    for ctry in vacdatas:
        ret.append((ctry["country"],
                    ctry["timeline"]["7/3/21"]))
    return ret


def countrycheck():
    arr1 = []
    arr2 = []
    for ctry in datas:
        arr1.append(ctry["country"])
    for ctry in vacdatas:
        arr2.append(ctry["country"])
    if (len(arr1) == len(arr2)):
        for i in range(len(arr1)):
            if (arr1[i] != arr2[i]):
                print("not same")
                return 0
        print("same")
        return 1
    else:
        if (len(arr1) > len(arr2)):
            print("arr1 is longer")
            print(len(arr1), len(arr2))
        else:
            print("arr2 is longer")
        for i in range(min(len(arr1),len(arr2))):
            print(arr1[i],arr2[i])

def getProhibitionInformation():
    ret = []
    prohibitCtry = ['Taiwan', 'New Zealand', "Lao People's Democratic Republic", 'Macao', 'Malaysia', 'Vietnam', 'Japan', 'Indonesia', 'Singapore', 'Philippines', 'Hong Kong', 'Australia', 'Argentina', 'Uruguay', 'Chile', 'Canada', 'Norway', 'Hungary', 'Cameroon', 'Congo', 'Algeria', 'Israel', 'Oman', 'Palestine']
    ctryInform = getCountriesInformation()
    for ctry in ctryInform:
        for pro_ctry in prohibitCtry:
            if ctry[0] == pro_ctry:
                ret.append(ctry)
    return ret

def getImpossibleTravel():
    ret = []
    prohibitTravel = ['Iraq', 'Syrian Arab Republic', 'Libyan Arab Jamahiriya', 'Somalia', 'Yemen']
    ctryInform = getCountriesInformation()
    for ctry in ctryInform:
        for pro_ctry in prohibitTravel:
            if ctry[0] == pro_ctry:
                ret.append(ctry)
    return ret

def getPossibleTravel():
    prohibitTravel = ['Iraq', 'Syrian Arab Republic', 'Libyan Arab Jamahiriya', 'Somalia', 'Yemen']
    ctryInform = getCountriesInformation()
    for ctry in ctryInform:
        for pro_ctry in prohibitTravel:
            if ctry[0] == pro_ctry:
                ctryInform.remove(ctry)
    return ctryInform



#코로나 관련 정보 받아오는 곳
# 222개 지역
headers = {
            'accept': 'application/json',
          }

params =  (
          )

response = requests.get('https://disease.sh/v3/covid-19/countries', headers=headers, params=params)
datas = response.json()

#백신 관련 정보 받아오는 곳
# 211개 지역
headers = {
            'accept': 'application/json',
          }

params =  (
            ("lastdays","1"),
            ("fullData","false"),
          )

response = requests.get('https://disease.sh/v3/covid-19/vaccine/coverage/countries', headers=headers, params=params)
vacdatas = response.json()

#countrycheck()
