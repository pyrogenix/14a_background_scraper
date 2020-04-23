import os
import subprocess
import re
import PyPDF2 as p2
import pdfquery
import requests
import unicodedata
from bs4 import BeautifulSoup

for root, dirs, files in os.walk('./14a_pdf', topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

