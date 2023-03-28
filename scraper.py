import requests
from bs4 import BeautifulSoup

def get_titles_from_url(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    titles = [title.get_text() for title in soup.find_all("h2")]
    return titles

if __name__ == "__main__":

	url='https://www.hectormainar.com/h1.php'
	
	titles = get_titles_from_url(url)

	print("Títulos encontrados:")

	for title in titles:
		print(title)


#https://www.hectormainar.com/h1.php