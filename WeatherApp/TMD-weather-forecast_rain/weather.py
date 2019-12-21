import json   
# urllib.request to make a request to api 
import requests
from jinja2 import Template
import pandas as pd
from datetime import datetime
from datetime import date
import sys 

def daily_openweather(location):
    api_key = [API KEY]
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    
    return r.json()

# Forcast 7 วัน กรมอุตุนิยมวิทยา
def forcast_tmd(amphoe="",province="สมุทรปราการ"):
    url = "https://data.tmd.go.th/api/WeatherForecast7Days/V1/"

    querystring = {"province":{province}, "amphoe":{amphoe}}

    headers = {
        'accept': "application/json",
        'authorization': [SENSOR]
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    return data
