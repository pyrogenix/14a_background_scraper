import re
import sys
import xlsxwriter

# txtfile = open("output.txt", "rt")
# contents = txtfile.read()

# listed = []

# with open("output.txt", "rt") as text:
#     Line = text.readline()

#     while Line!='':
#         Line1 = Line.split('.')
#         for Sentence in Line1:
#             listed.append(Sentence)
#         Line = text.readline()
# print(listed)

# month = {'january', 'february', 'march', 'april', 'may', 'june'}
# stringToMatch = 'month'
# matchedLine = ''
# #get line
# with open('output.txt', 'r') as file:
# 	for line in file:
# 		if stringToMatch in line:
# 			matchedLine = line
# 			break
# #and write it to the file
# with open('file.txt', 'w') as file:
# 	file.write(matchedLine)

# import datefinder

# with open('output.txt', 'rt') as filingtxt:
#         data = filingtxt.readlines()

# matches = datefinder.find_dates(str(data))
# for match in matches:
#     print(match)

file_name = './a2231072zdefm14a.htm'

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
matched_lines = search_multiple_strings_in_file(file_name, ['background of the merger', 'termination fee'])
 
print('Total Matched lines : ', len(matched_lines))
for elem in matched_lines:
    # sys.stdout = open('file.htm','wt')
    print('Word = ', elem[0], ' :: Line Number = ', elem[1], ' :: Line = ', elem[2])


#excel
workbook = xlsxwriter.Workbook('./output.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'CIK')
worksheet.write('B1', 'URL')
worksheet.write('C1', 'Search Term')
worksheet.write('D1', 'Results')

row = 0
column = 2

search_term = (elem[0])
data_output = (elem[2])

for item in search_term:
    worksheet.write(row + 1, column, item)

column = 3

for item in data_output:
    worksheet.write(row + 1, column, item)

workbook.close()