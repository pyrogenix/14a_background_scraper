import urllib.request, urllib.error, urllib.parse
import re
import requests
import sys
import xlsxwriter
import soupsieve
import pandas as pd
from xlrd import open_workbook
from bs4 import BeautifulSoup
from urllib.request import urlopen

test_link = 'https://www.sec.gov/Archives/edgar/data/1062613/000104746917000993/a2231072zdefm14a.htm'

res = requests.get(test_link)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
for s in soup:
    text = soup.find_all('b', text=True)
#print(text)

output = ''
blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script',
	# there may be more elements you don't want, such as "style", etc.
]


for t in text:
	if t.parent.name not in blacklist:
		output += '{} '.format(t)

# for t in text(text=re.compile(r'Background( |&nbsp;)(o|O)f( |&nbsp;)(t|T)he')):
#     print(t)

print(output)