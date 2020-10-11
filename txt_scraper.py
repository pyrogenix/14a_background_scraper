import os
import re

txtdir = "./output_as_txt/"
for file in os.scandir(txtdir):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # output = open('txt_scr_out_test.txt', 'w', encoding='utf-8')
    # output.write(content)
    f.close()
