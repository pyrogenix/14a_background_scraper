import re
import requests
import unicodedata
from bs4 import BeautifulSoup

# Some code from areed1192 AKA Sigma Coding

# Possible even better solution
""" IDEAS:
    Go by pages. Start at BOTM page (next anchor). 
    End at page before next section starts. Extract all
    text within there (by <p>?)
"""

base_url = r"https://sec.gov/Archives/edgar/data"
