import requests
import json
# city=input('Enter city you wanna know info about = ')
city='jaipur'
url=f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&include=days&key=J7F7C3ZARBJ5UUYDZH7V7HH3Z&contentType=json'
r=requests.get(url)
wdit=json.loads(r.text)
print(f'\nHere is all the important information about weather conditions of city of {city}\n')
temp=wdit['days'][0]['temp']
date_time=wdit['days'][0]['datetime']
feellike_temp=wdit['days'][0]['feelslike']
tempmax=wdit['days'][0]['tempmax']
des=wdit['days'][0]['description']
print(f'On a date of {date_time}(YYYY-MM--DD) temp is {temp} with max temp of day is {tempmax} and it fells like {feellike_temp}\nhence the overall description is \"{des}\"\n')
