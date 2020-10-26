import os
import re

# WARNING:
# Code is unfinished and scrapped.
# Don't bother trying to use it.


def main():
    txtdir = "./output_as_txt/"
    for file in os.scandir(txtdir):
        lines = []
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                curr_line = f.readline()
                lines.append(curr_line)
        potential_matches = ['background of the merger',
                             'background to the merger', 'background']
        lines_to_investigate = []
        for i in range(len(lines)):
            for j in potential_matches:
                if j in lines[i].lower():
                    print(f'Potential Match at line {i} in {file}:')
                    print(lines[i])
                    lines_to_investigate.append(i)
        lines_to_investigate.sort()
        try:
            lines_num = lines_to_investigate[-1]
        except:
            break
        scrape_dates(lines, lines_num)
        # output = open('txt_scr_out_test.txt', 'w', encoding='utf-8')
        # output.write(content)
        f.close()


def scrape_dates(line_list, line_num):
    curr_line = line_list[line_num]
    for line in line_list[line_num:]:
        pattern = re.findall(
            r"([A-Z][a-z]{3,9} [0-9]{1,2}([a-z][a-z]|, )201[0-9])", line)
        if pattern != []:
            print(line)

    # pattern = re.compile(
    #     r"([A-Z][a-z]{3,9} [0-9]{1,2}([a-z][a-z]|, )201[0-9])")
    # matches = pattern.finditer(str(curr_line))
    # print(matches)
    # print(pattern)


if __name__ == "__main__":
    main()


# ([A-Z][a-z]{3,9} [0-9]{1,2}([a-z][a-z]|, )201[0-9])
# [A-Z][a-z]{3,9}( |&nbsp;)[0-9]{1,4} << old ^^ better
