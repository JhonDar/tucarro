import requests
from bs4 import BeautifulSoup
 
base_page = requests.get('https://listado.tucarro.com.co/camionetas')
soup = BeautifulSoup(base_page.text, "lxml")
found_next = True

while found_next:
		for i in soup.findAll("div", {"class": "rowItem"}):
			h2_tag = i.find("h2", {"class": "list-view-item-title"})
			for a_tag in h2_tag.find_all('a',href=True):
				car_link = a_tag["href"]
				car_page = requests.get(car_link)
				soup_car = BeautifulSoup(car_page.text, "lxml")
				price = soup_car.find("span", {"class": "price-tag-fraction"}).text
				print(price)

		li_tag = soup.find("li", {"class": "last-child"})

		if li_tag is not(None):
			for a_tag in li_tag.find_all('a',href=True):
				next_page=a_tag["href"]
				base_page = requests.get(next_page)
				soup = BeautifulSoup(base_page.text, "lxml")
		else:
			found_next = False


