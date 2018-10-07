import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://news.yandex.ru/index.html')
soup = BeautifulSoup(html_doc.text, 'html.parser')
soup = soup.find_all(class_='story__topic')
for row in soup:
	print(row.prettify())