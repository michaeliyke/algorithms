"""
  http://quotes.toscrape.com/
"""

import re
from bs4 import BeautifulSoup as Bs
from requests import get

dots, br = " ------------------------------------", "\n"

def scrape():
  pg = Bs(get("http://quotes.toscrape.com/").text, "lxml")
  title = pg.select_one("h1 a")
  show(br, dots, title.text, dots, br)
  for q in pg.find_all("div", class_="quote"):
    showQuote(q)


def show(*texts) -> None:
  print(*texts)


def showQuote(q):
  text = q.find("span", class_="text").text
  author = q.find("small", class_="author").text
  regex = re.compile(r"\W+", re.IGNORECASE) # Attempt removing newline
  st = ", ".join(
    regex.sub(" ", t.text) for t in q.find_all("a", class_="tag")
    )

  print(br, text, br, "Author: "+author, br, "Tags:",st, br*2)
