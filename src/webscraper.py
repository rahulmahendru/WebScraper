import requests 
from bs4 import BeautifulSoup

def getHTML(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    file = open("HTML_file.txt", "x")
    file.write(soup.prettify())
    file.close()

def getXML(page):
    soup = BeautifulSoup(page.content, 'lxml')
    file = open("XML_file.txt", "x")
    file.write(soup.prettify())
    file.close()

URL = input("Enter a URL: ")
page = requests.get(URL)
getHTML(page)
getXML(page)