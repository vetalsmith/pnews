import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://news.yandex.ru/index.html')
soup = BeautifulSoup(html_doc.text, 'html.parser')
print(soup.prettify())