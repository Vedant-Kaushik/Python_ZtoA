import requests
import json

query=input('what kind of news do you want = ')
date=input('enter date (DD) = ')

for i in range(0,2):
  print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
  apikey=f'https://newsapi.org/v2/everything?q={query}&from=2024-04-{date}&sortBy=publishedAt&apiKey=760ab34bf62c4b69b0b330971c9ac89a'

url= apikey
r=requests.get(url)
news=json.loads(r.text)

i=1
for article in news['articles']:
  print(f'{i})','Title = ',article['title'])
  print('\t','Description = ',article['description'])
  print('------------------------------------------------------------------------------------------------------')
  i+=1.      