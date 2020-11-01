""" PDF to TXT converter designed for use in the 14A Background Scraper project.
    Version 3.0.0
"""

from tika import parser
import os


# WARNING: THE CURRENT VERSION OF THIS CODE IS UNTESTED AND IS
# JUST A SHORTENED EDIT OF THE PREVIOUS PROGRAM
# FOR GUARANTEED WORKING CODE USE ./old/pdf_txt_converter_long.py

def convert_to_txt():
    # Uses Tika parser to open each file and convert to txt
    pdf_dir = './14a_pdf/'
    for file in os.scandir(pdf_dir):
        try:
            raw = parser.from_file('./14a_pdf/' + file)
        except Exception:
            print("ERROR: " + file + " failed to convert.")
        output = open('./output_as_txt/' + file +
                      '.txt', 'w', encoding='utf-8')
        output.write(str(raw['content']))
        print("Successfully converted " + file + " to .txt")


if __name__ == "__main__":
    convert_to_txt()
