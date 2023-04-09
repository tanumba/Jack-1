import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL_TEMPLATE = "https://23city.ru/contact/"
response = requests.get(URL_TEMPLATE)
bs1 = bs(response.text, 'html.parser')
temp = bs1.find_all('p', 'content-icon-spacing')
for i in temp:
    print(i.text) 