'''
A simple scraper using Python Requests and Beautiful Soup
'''

import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

try:
    page = requests.get("https://nickclegg.medium.com/making-the-metaverse-what-it-is-how-it-will-be-built-and-why-it-matters-3710f7570b04")
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup)
    #for link in soup.find_all('a', href=True):
    #   print(link['href'])
    #paras = soup.find_all('p', {'class': "pw-post-body-paragraph"})
    #print(paras)
except HTTPError as http_err: 
    print(f"HTTP error occurred: {http_err}") 
except Exception as err: 
    print(f"Other error occurred: {err}")