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

# basepath = './14a_pdf'
# for fname in os.listdir(basepath):
#     path = os.path.join(basepath, fname)
#     if os.path.isdir(path):
#         continue
# print(path)

# print(fitz.__doc__)

pdfminer.__version__

filename='./14a_pdf/2634022020_BEAERO_14A_20170302.pdf'
# with open(filename) as file_obj:
#     for line in file_obj:
#         print(line.strip())

# class Document:
#     def __init__(self, filename='./14a_pdf/2732707020_FAIRPOINT_14A_20170227.pdf'):
#         UserDict.__init__(self)
        
# text = []
# doc = fitz.open('./14a_pdf/2732707020_FAIRPOINT_14A_20170227.pdf') 
# #Document.getToC(simple=True)
# for page in doc:
#     t = page.getText().encode("utf8")
#     text.append(t)
# print(text)

def pdf_to_csv(filename):
    from io import StringIO  
    from pdfminer.converter import LTChar, TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfparser import PDFDocument, PDFParser
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

    class CsvConverter(TextConverter):
        def __init__(self, *args, **kwargs):
            TextConverter.__init__(self, *args, **kwargs)

        def end_page(self, i):
            from collections import defaultdict
            lines = defaultdict(lambda : {})
            for child in self.cur_item._objs:                #<-- changed
                if isinstance(child, LTChar):
                    (_,_,x,y) = child.bbox                   
                    line = lines[int(-y)]
                    line[x] = child._text.encode(self.codec) #<-- changed

            for y in sorted(lines.keys()):
                line = lines[y]
                self.outfp.write(";".join(line[x] for x in sorted(line.keys())))
                self.outfp.write("\n")

    # ... the following part of the code is a remix of the 
    # convert() function in the pdfminer/tools/pdf2text module
    rsrc = PDFResourceManager()
    outfp = StringIO()
    device = CsvConverter(rsrc, outfp, codec="utf-8", laparams=LAParams())
        # becuase my test documents are utf-8 (note: utf-8 is the default codec)

    doc = PDFDocument()
    fp = open(filename, 'rb')
    parser = PDFParser(fp)       
    parser.set_document(doc)     
    doc.set_parser(parser)       
    doc.initialize('')

    interpreter = PDFPageInterpreter(rsrc, device)

    for i, page in enumerate(doc.get_pages()):
        outfp.write("START PAGE %d\n" % i)
        if page is not None:
            interpreter.process_page(page)
        outfp.write("END PAGE %d\n" % i)

    device.close()
    fp.close()

    return outfp.getvalue()