import requests 
from bs4 import BeautifulSoup


URL = input("Enter a URL: ")
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())