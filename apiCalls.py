import requests
import json

baseUrl = "https://api.upcitemdb.com/prod/trial/lookup"
parameters = { "upc": "0885909950805"}

response = requests.get(baseUrl, params=parameters)
content = response.content
info = json.loads(content.decode("utf-8"))

items = info["items"]
itemInfo = items[0]
title = itemInfo["title"]
brand = itemInfo["brand"]
print(title, brand)
