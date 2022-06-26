import requests
from bs4 import BeautifulSoup

response = requests.get(
	url=input('Ingresa URL de wikipedia que necesitar scrapear: '),
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.string)