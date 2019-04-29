from requests_html import HTMLSession
from bs4 import BeautifulSoup


def extract(url):
    session = HTMLSession()
    response = session.get(url)
    response.html.render()
    soup = BeautifulSoup(response.html.html, features="html.parser")
    result = []
    for hit in soup.find_all("h2", {"class": "item-title"}):
        result.append(hit.contents[0].strip())

    return result
