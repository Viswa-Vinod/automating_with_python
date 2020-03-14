from bs4 import BeautifulSoup
import requests

baseUrl = "https://scrapingclub.com/exercise/list_basic/?page=1"
response = requests.get(baseUrl)
soup = BeautifulSoup(response.text, "lxml")
items = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
count = 1
for i in items:
    itemName = i.find("h4", class_ = "card-title").text.strip("\n")
    itemPrice = i.find("h5").text
    print("(%s ) Price: %s, Item Name: %s" %(count, itemPrice, itemName))
    count = count + 1

pages = soup.find("ul", class_="pagination")
urls = []
links = pages.find_all("a", class_="page-link")
for link in links:
    # pageNum will be none if the value of link.text is next or previous
    # or it will be cast into an integer if it is one of the value 1, 2, 3 and so on
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get("href")
        urls.append(x)
count = 1
for url in urls:
    newUrl = baseUrl + url
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, "lxml")
    items = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
    
    for i in items:
        itemName = i.find("h4", class_ = "card-title").text.strip("\n")
        itemPrice = i.find("h5").text
        print("(%s ) Price: %s, Item Name: %s" %(count, itemPrice, itemName))
        count = count + 1    
