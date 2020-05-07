import re
import sys
import xlsxwriter
import soupsieve
import urllib.request, urllib.error, urllib.parse
import pandas as pd
from xlrd import open_workbook
from bs4 import BeautifulSoup

# with open(htm_links.xlsx, 'r') as text:

# file_name = './a2230778zdefm14a.htm'
# with open(file_name, 'r') as text:
#         for line in txtt:
#         linenum +=1
#         pattern = re.compile(r'July')
#         matches = pattern.finditer(str(txtt))
#         for match in matches:
#             print(match)
count = 0

data = pd.read_excel(r'htm_links.xlsx')
df = pd.DataFrame(data, columns = ['url', 'file'])
# print(df['url'][0])

# "[A-Z][a-z]*\s\d{1,2}[,\/]\s\d{4}"

workbook = xlsxwriter.Workbook('./output_extractor-v2.xlsx')

worksheet = workbook.add_worksheet()
worksheet.write('A1', 'CIK')
worksheet.write('B1', 'URL')
worksheet.write('C1', 'Search Term')
worksheet.write('D1', 'Results')

row = 0
column = 2

for cell in data: 
    file_url = df['url'][count]
    print(file_url)

    linenum = 0
    for line in urllib.request.urlopen(file_url):
        linenum +=1
        pattern = re.compile(r"[A-Z][a-z]{3,9}")
        matches = pattern.finditer(str(urllib.request.urlopen(file_url)))

        # if matches in line:
        #     print(line.rstrip())

        for match in matches:
            print(match)
            #print(line.rstrip())

            dataline = line.rstrip()

            worksheet.write(row + 1, column, str(match))
            worksheet.write(row + 1, column +1, str(dataline))
            column += 1

    count+= 1
    continue

workbook.close()