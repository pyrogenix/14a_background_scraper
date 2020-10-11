import urllib.request, urllib.error, urllib.parse
import re
import sys
import xlsxwriter
import soupsieve
import pandas as pd
from xlrd import open_workbook
from bs4 import BeautifulSoup
from urllib.request import urlopen

workbook = xlsxwriter.Workbook('./output_extractor-v3.xlsx')

worksheet = workbook.add_worksheet()
worksheet.write('A1', 'CIK')
worksheet.write('B1', 'URL')
worksheet.write('C1', 'Search Term')
worksheet.write('D1', 'Results')

row = 0
column = 2

def getLinks(url):
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, 'html.parser')
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile(r"#dc[0-9]{5}_background_of_the_merger")}):
        links.append(link.get('href'))

    return links

data = pd.read_excel(r'htm_links.xlsx')
df = pd.DataFrame(data, columns = ['url', 'file'])

count = 0

runner = 0
while True:
    for cell in data: 
        raw_url = df['url'][count]
        docu = urlopen(raw_url)
        soup = BeautifulSoup(docu.read(), 'html.parser')
        # print(raw_url)

        link_tag = getLinks(raw_url)
        file_url = str(raw_url) + str(link_tag[1])
        print(file_url)

        #***start excel
        for cell in data: 
            linenum = 0
            for line in urllib.request.urlopen(file_url):
                linenum +=1
                pattern = re.compile(r"[A-Z][a-z]{3,9}( |&nbsp;)[0-9]{1,4}")
                matches = pattern.finditer(str(urllib.request.urlopen(file_url)))

                # if matches in line:
                #     print(line.rstrip())

                for match in matches:
                    print(match)
                    print(line.rstrip())

                    dataline = line.rstrip()

                    worksheet.write(row + 1, column, str(match))
                    worksheet.write(row + 1, column +1, str(dataline))
                    column += 1

            count+= 1
            continue

        workbook.close()
        #***end excel

        count+= 1
        if file_url == '':
            runner  = 1
        continue