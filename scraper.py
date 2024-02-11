import requests
import re
from bs4 import BeautifulSoup

URL = 'https://www.fotmob.com/'

page = requests.get(URL)


def get_title():
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find("div", class_="crayons-story__body")
    title = post .find("h2", class_="crayons-story__title").text.strip()

    return title+'\nFor full article visit DEV.TO '