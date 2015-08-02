import requests
from bs4 import BeautifulSoup as bs
p = requests.get('http://www.manta.com/world/Oceania/Australia/')
s = bs(p.text)
title = s.find('span', attrs={'itemprop':'title'}).text
print title
