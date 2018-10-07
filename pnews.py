import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://news.yandex.ru/index.html')
soup = BeautifulSoup(html_doc.text, 'html.parser')
divs = soup.select('.story__topic')
h2 = soup.select('.story__topic .story__title a')
for row in h2:
	print(row.getText())