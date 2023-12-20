from googlesearch import search
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

def is_title_valid(title):
    # Проверяем, что в строке нет непонятных символов
    # Это можно сделать, сравнивая строку после декодирования .encode().decode()
    try:
        return title.encode('ascii').decode('ascii') == title
    except UnicodeEncodeError:
        return False
def SERP(query):
    data = []
    for i in search(query, tld="co.in", num=1, stop=15, pause=0.1):
        a = get_article_title(i)
        if a is not None:
            a = a.strip()
            data.append([a, i])
    return data
def get_article_title(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('title')

        result = title_tag.get_text() if title_tag else None
    except requests.exceptions.RequestException as e:
        return None

    return result