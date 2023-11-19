
import requests
from bs4 import BeautifulSoup as bs

link = 'https://static.cricinfo.com/rss/livescores.xml'
req = requests.get(link)

soup = bs(req.content, 'xml')
box = soup.findAll('title')

for i in box:
    if 'india' in i.text.lower():
        print(i.text)
