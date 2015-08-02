import urllib2
from bs4 import BeautifulSoup as bs
p = requests.get('http://www.manta.com/world/Oceania/Australia/')
s = bs(p)
title = s.find('span', attrs={'itemprop':'title'}).text
print title
