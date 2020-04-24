import os
import subprocess
import re
import PyPDF2 as p2
import pdfquery
import requests
import unicodedata
import pdfminer
import fitz
from bs4 import BeautifulSoup

#for root, dirs, files in os.walk('./14a_pdf', topdown=False):
#    for name in files:
#        print(os.path.join(root, name))
#    for name in dirs:
#        print(os.path.join(root, name))

basepath = './14a_pdf'
for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if os.path.isdir(path):
        continue
print(os.path.join(basepath, fname))

print(fitz.__doc__)
#class Document
#    __init__(filename='./14a_pdf/2732707020_FAIRPOINT_14A_20170227.pdf')
#fitz.Document('./14a_pdf/2732707020_FAIRPOINT_14A_20170227.pdf') 
Document.getToC(simple=True)
Document.pageCount()