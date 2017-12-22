import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def parse(html):
	soup = BeautifulSoup(html,"html.parser")
	names = soup.find('ol')
	#print(news.prettify())
	news = []
	for a in names.find_all('a'):
		#label = a.find_all('aria-label')
		news.append(
			a.text
			)

	return news


def get_info():
	return parse(get_html('https://yandex.ru'))