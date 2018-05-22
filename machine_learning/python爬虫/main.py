#!usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html=urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
            ).read().decode()
#res=re.findall(r"<title>(.+?)</title>",html)
#links=re.findall(r'href="(.*?)"', html)

soup=BeautifulSoup(html,features="lxml")
print(soup.h1)
#print(html)

#all_href = soup.find_all('a')
all_href = [li['href'] for li in soup.find_all('a')]
print('\n', all_href)