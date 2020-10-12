""" PDF to TXT converter designed for use in the 14A Background Scraper project.
    Author: Adam Heitzman (pyrogenix)
    Version 2.0.0
"""

# MUCH OF THIS CODE IS REDUNDANT AND IS NOT NEEDED
# IT COULD EASILY BE SHORTENED BUT I HAVE FINISHED
# THIS CONVERSION JOB SO I HAVE NO REASON TO OPTIMIZE IT

from tika import parser
import pandas as pd


def get_pdfs():
    # Opens excel sheet and creates dataframe using column 'Filename'
    file_count, error_count, error_log = 0, 0, []
    spreadsheet = pd.read_excel(r'file_list.xlsx')
    df = pd.DataFrame(spreadsheet, columns=['Filename'])

    # Iterates through rows in dataframe and extracts the
    # file name from all the info returned
    for index, row in df.iterrows():
        file_holder = str(row).split()
        curr_file = file_holder[1]
        if '14A' in curr_file:
            error_count, error_log = convert_to_txt(
                curr_file, error_count, error_log)
            file_count += 1

    # Prints end of program message
    if error_count == 0:
        print("All files successfully converted")
    else:
        print(str(error_count) + " out of " +
              file_count + " files successfully converted")
        print("The following files were unable to convert: ")
        for i in error_log:
            print("> " + i)
    exit()


def convert_to_txt(file_name, error_count, error_log):
    # Uses Tika parser to open each file and convert to txt
    try:
        raw = parser.from_file('./14a_pdf/' + file_name)
    except Exception:
        print("ERROR: " + file_name + " failed to convert.")
        error_count += 1
        error_log.append(file_name)
    output = open('./output_as_txt/' + file_name +
                  '.txt', 'w', encoding='utf-8')
    output.write(str(raw['content']))
    print("Successfully converted " + file_name + " to .txt")
    return error_count, error_log


if __name__ == "__main__":
    get_pdfs()
