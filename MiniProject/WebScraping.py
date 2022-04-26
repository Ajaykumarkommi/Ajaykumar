from bs4 import BeautifulSoup
import requests
import os

html_text = requests.get("https://www.flipkart.com/search?q=smartwatch&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=smartwatch%7CSmart+Watches&requestId=c06e5ea0-2e19-4992-afd6-c3e95bc27176&as-backfill=on")
soup = BeautifulSoup(html_text.text, "lxml")
res = soup.findAll("div", class_= "_3pLy-c row")
html ="<center>"
html +="<h1>"+"Product Table"+"</h1>"
html += f'<table border={1}">'
html += "<tr>"
html += "<th>" + "product name" +"</th>"
html += "<th>" + "product price" + "</th>"
html += "<th>" + "rating" + "</th>"
html += "<th>" + "discount" + "</th>"
html += "</tr>"
html += "<tr>"
for result in res:
    prod = result.find("div", class_="_4rR01T").text
    price = result.find("div", class_="_30jeq3 _1_WHN1").text
    rating = result.find("div",class_="_3LWZlK").text
    disc = result.find("div",class_="_3Ay6Sb").find("span").text

    # print(rating,prod,price,offer)
    html += "<td>" + prod + "</td>"
    html += "<td>" + price + "</td>"
    html += "<td>" + rating + "</td>"
    html += "<td>" + disc + "</td>"
    html += "</tr>"
html += "</table>"
html +="</center>"
with open("outpt.html", "w", encoding='utf-8') as file:
    file.write(html)

os.startfile('outpt.html')
