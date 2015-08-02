import urllib2
from bs4 import BeautifulSoup as bs
p = urllib2.urlopen('http://www.manta.com/world/Oceania/Australia/')
s = bs(p)
title = s.find('span', attrs={'itemprop':'title'}).text
print title
