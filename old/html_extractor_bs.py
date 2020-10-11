import re
import sys
import xlsxwriter
import soupsieve
import urllib.request, urllib.error, urllib.parse
import pandas as pd
from xlrd import open_workbook
from bs4 import BeautifulSoup
from urllib.request import urlopen

data = pd.read_excel(r'htm_links.xlsx')
df = pd.DataFrame(data, columns = ['url', 'file'])

count = 0

runner = 0
while True:
    for cell in data: 
        file_url = df['url'][count]
        docu = urlopen(file_url)
        soup = BeautifulSoup(docu.read(), 'html.parser')
        print(file_url)

        for p in soup.find('p', text='merger').find_next_siblings('p'):
            print(p.text)
        # outfile = open('.texport.txt', 'w')
        # outfile.write(p.text)

        count+= 1
        if file_url == '':
            runner  = 1
        continue