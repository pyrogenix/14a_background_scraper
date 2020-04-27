from io import BytesIO
from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

rsrcmgr = PDFResourceManager()
sio = BytesIO()
codec = 'utf-8'
laparams = LAParams()
device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

fp = open('./14a_pdf/2634022020_BEAERO_14A_20170302.pdf', 'rb')
for page in PDFPage.get_pages(fp):
    interpreter.process_page(page)
fp.close()
text = sio.getvalue()
#text=text.replace(chr(272)," ")
print(type(text))
f = open('./output.txt','w')
f.write(str(text))

print("hello")