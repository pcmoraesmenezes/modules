import requests 
from bs4 import BeautifulSoup
import re

url = 'http://localhost:3333/'

response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')


seletor = parsed_html.select_one('body > h1')
print(parsed_html.title.text)
print(seletor.text)

if seletor is not None:
    article = seletor.parent

    if article is not None:
        for p in article.select('h1'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())
