import re
import sys
import xlsxwriter
import soupsieve
import urllib.request, urllib.error, urllib.parse
from xlrd import open_workbook
from bs4 import BeautifulSoup

#file_name = './a2231072zdefm14a.htm'
file_name = './a2230778zdefm14a.htm'

# url = 'https://www.sec.gov/Archives/edgar/data/861361/000104746917000512/a2230778zdefm14a.htm'

# book = open_workbook('url.xlsx', on_demand = True)
# for name in book.sheet_names():
#     if name.endswith('.htm'):
#         sheet = book.sheet_by_name(name)
#         rowIndex = -1
#         for cell in sheet.col(0): 
#             if '.htm' in cell.value:
#                 break

#         if row != -1:
#             cells = sheet.row(row)
#             for cell in cells:
#                 print(cell.value)

#         book.unload_sheet(name) 

# response = urllib.request.urlopen(url)
# webContent = response.read()

sec_htm = 'a2230778zdefm14a.htm#'

# f = open(sec_htm, 'wb')
# f.write(webContent)
# f.close

# filename = urllib.parse.urlsplit(url, scheme='', allow_fragments=True)
# print(filename[2])
# print(webContent)



month = ['July', 'August', 'july', 'august']
space = [' ', '&nbsp;']
day = ['7']
nth = ["", "st", "nd", "rd", "th"]
year = ['2016']
#datee = [month[-0:] + space[1] + day[-0:] + ',' + space[0] + year[0]]
#print(datee)

def search_multiple_strings_in_file(file_name, list_of_strings):
    """Get line from the file along with line numbers, which contains any string from the list"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for string_to_search in list_of_strings:
                if string_to_search in line:
                    # If any string is found in line, then append that line along with line number in list
                    list_of_results.append((string_to_search, line_number, line.rstrip()))
 
    # Return list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results

# search for given strings in the file 'sample.txt'
matched_lines = search_multiple_strings_in_file(file_name, month)


print('Total Matched lines : ', len(matched_lines))
for elem in matched_lines:
    # sys.stdout = open('file.htm','wt')
    print('Word = ', elem[0], ' :: Line Number = ', elem[1], ' :: Line = ', elem[2])

linenum = 0
with open(file_name, 'r') as txtt:
    for line in txtt:
        linenum +=1
        pattern = re.compile(r'\d')
        matches = pattern.finditer(str(txtt))
        for match in matches:
            print(match)

# excel
workbook = xlsxwriter.Workbook('./output.xlsx')

worksheet = workbook.add_worksheet()
worksheet.write('A1', 'CIK')
worksheet.write('B1', 'URL')
worksheet.write('C1', 'Search Term')
worksheet.write('D1', 'Results')

row = 0
column = 2

worksheet.write(row + 1, column, str(elem[0]))

for elem in matched_lines[:50]:
    worksheet.write(row + 1, column +1, str(elem[2]))
    column += 1

workbook.close()

if any(line in file_name for line in month):
    print(file_name)