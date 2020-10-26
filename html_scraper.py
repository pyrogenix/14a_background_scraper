import os
import re
import requests
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path

# Possible better solution


def main():
    # file = './old/a2231072zdefm14a.htm'
    file = './old/a2230778zdefm14a.htm'
    with open(file) as f:
        soup = BeautifulSoup(f)
    foundBg = False
    for link in soup.findAll("a"):
        anchor_txt = link.text
        anchor = link.get("href")
        matchFound = False
        background_terms = ['background of the merger',
                            'background to the merger']
        if foundBg == True:
            next_pt = file + anchor
            if anchor_txt
            # Refine this if needed.
            break
        elif not anchor == None:
            for i in background_terms:
                if i in anchor_txt.lower():
                    matchFound = True
                    certain = True
                    goto_bg(file, anchor_txt, anchor, certain)
                    foundBg = True
                    break

            if matchFound == False:
                if "background" in anchor_txt.lower():
                    certain = False
                    goto_bg(file, anchor_txt, anchor, certain)
                    foundBg = True

    extract_bg()


def goto_bg(file, anchor_txt, anchor, certain):
    assert certain, 'WARNING: Background may not be correct. Please manually check.'
    bg_url = file + anchor
    print(bg_url)
    print('--')
    # src = urllib3.request.open(bg_url).read()
    src = urljoin(file, anchor)
    print(src)
    print('..')

    # response = requests.get(src)

    # soup = BeautifulSoup(response.content, "html.parser")
# aaa = BeautifulSoup.find_all(file_with_toc, 'Backgrounnd')


def extract_bg():
    pass


if __name__ == "__main__":
    main()
