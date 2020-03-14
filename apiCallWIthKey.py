import requests
import json

API_KEY = "dummy api key" #signup to openweathermap and get an api key for your account
baseUrl = "http://api.openweathermap.org/data/2.5/forecast"
parameters = { "q": "Seattle,US", "APPID": API_KEY}

response = requests.get(baseUrl, params=parameters)
content = response.content
info = json.loads(content.decode("utf-8"))
