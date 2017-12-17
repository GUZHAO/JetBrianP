import requests
from bs4 import BeautifulSoup
from pprint import pprint
import timeit

prefix = "http://www.upneat.rocks"

#http://www.upneat.rocks/recipe/sources/the-craft-of-the-cocktail --recipes style not in sync
#http://www.upneat.rocks/recipe/sources/pdt --recipe style not in sync
#http://www.upneat.rocks/recipe/sources/death-co -- potentially missing recipes

c_href = BeautifulSoup(requests.get('http://www.upneat.rocks/recipe/sources/death-co').text, 'html.parser').\
              select('a[href^="/recipes/"]')
         # BeautifulSoup(requests.get('http://www.upneat.rocks/recipe/sources/pdt').text, 'html.parser'). \
         #     select('a[href^="/recipes/"]') + \
         # BeautifulSoup(requests.get('http://www.upneat.rocks/recipe/sources/the-craft-of-the-cocktail').text, 'html.parser'). \
         #     select('a[href^="/recipes/"]')

c_link = []
for link in c_href:
    c_link.append(link.get('href'))

#pprint(c_link)

c_name = []
for element in c_href:
    c_name.append(element.get_text())

#pprint(c_name)

c_data= {}
c_data['data'] = []

for element in c_link:
    url = "http://www.upneat.rocks{}".format(element)
    c_url = BeautifulSoup(requests.get(url).text, 'html.parser')
    c_recipe = c_url.find('div', class_='col-md-12 col-lg-5').\
        find('ul').get_text(',', strip=True).split(',')
    c_method = c_url.find('div', class_='col-md-12 col-lg-5').\
        find('ul').next_sibling.next_sibling.get_text()
    c_data['data'].append({'link':url,'ingredient':c_recipe,'method':c_method})

pprint(c_data)

