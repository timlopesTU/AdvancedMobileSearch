import sys
from bs4 import BeautifulSoup
import requests

#Web Scrape with requests and BeautifulSoup

urls = []

with open("urls.txt") as f:
    urls = set(f.read().splitlines())

titleF = open("titles.txt", "w")

for url in urls:
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    title = soup.title.text
    title = title.split("<")[0].split("-")[0]
    title = title[:-1]
    titleF.write(title)
    titleF.write("\n")