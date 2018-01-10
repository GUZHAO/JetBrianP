import requests
from bs4 import BeautifulSoup
from pprint import pprint
import scrapy
import timeit
import pymongo

c_href = BeautifulSoup(
    requests.get('http://www.totalwine.com/spirits/gin/c/000870?storename=1701,1702,1703,1704,1502,1504,1503,1501,303,302&sort=name-asc').text, 'html.parser')

#print(c_href.prettify())

c_link = []
for link in c_href.select('a[href^="http://www.totalwine.com/spirits/gin//"]'):
    c_link.append(link.get('href'))
pprint(set(c_link)), pprint(len(set(c_link))) #pass

c_name = []
for element in c_href.select('a[class="analyticsProductName"]'):
    c_name.append(element.get_text())
#pprint(c_name), pprint(len(c_name)) #pass

c_quantity = []
for element in c_href.select('div[class="plp-product-qty"]'):
    c_quantity.append(element.get_text())
#pprint(c_quantity), pprint(len(c_quantity)) #pass on the condition that removing gift at the end

c_origin = []
for element in c_href.select('div[class="plp-product-loc"]'):
    c_origin.append(element.get_text().strip().replace(" | ", "|").replace("|Gin", ""))
#pprint(c_origin), pprint(len(c_origin)) #pass

c_desc = []
for element in c_href.select('span[class="winespec-desc-txt"]'):
    c_desc.append(element.get_text())
#pprint(c_desc) #double check

c_price = []
for element in c_href.select('span[class="price"]'):
    c_price.append(element.get_text())
#pprint(c_price)

url = c_link[0]
c_url = BeautifulSoup(requests.get(url).text, 'html.parser')
pprint(url)
pprint(c_url)