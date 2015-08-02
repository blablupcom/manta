import urllib2
import unirest
from bs4 import BeautifulSoup as bs
user_agent = {'User-Agent': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'}
p = unirest.get('http://www.manta.com/world/Oceania/Australia/', headers=user_agent)
s = bs(p)
title = s.find('span', attrs={'itemprop':'title'}).text
print title
