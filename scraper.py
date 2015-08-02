import urllib2
import requests
from bs4 import BeautifulSoup as bs
user_agent = {'User-Agent': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'}
p = requests.get('http://www.manta.com/world/Oceania/Australia/', headers=user_agent)
s = bs(p.text)
title = s.find('span', attrs={'itemprop':'title'}).text
print title
