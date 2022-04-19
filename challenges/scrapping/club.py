from bs4 import BeautifulSoup as Bs
from requests import get
import time

br = "\n "
host = "https://scrapingclub.com"
path = "/exercise/list_basic/"
index = 0

def _scrape(data):
  global index
  for item in data:
    link = host + item.find("a")["href"]
    img = host + item.find("img")["src"]
    title = item.find_all("a")[1].text
    price = item.find("h5").text
    index += 1
    print(
      br, "index: ", index,
      br, "link: ", link, 
      br, "image: ", img, 
      br, "title: ", title, 
      br, "price: ", price, 
      br,
      )

  

def _getNexts(paginationNav):
  cache = {}
  for pgItem in paginationNav.select("li.page-item"):
    href = "#" if pgItem.a == None else pgItem.a["href"]
    if "active" in pgItem["class"] or href == "#" or href in cache:
      continue
    cache[href] = pgItem.text
  return cache.keys()


def _getNext(paginationNav):
  res = paginationNav.select("li.page-item:last-of-type")
  nxt = res[0] if res != [] else None
  if not nxt or (not nxt.a) or nxt.a.text.lower() != "next": return ""
  return host + path + nxt.a["href"]


def paginate_2():
  pg = Bs(get(url=host+path).text, "lxml")
  pagination = pg.find("ul", class_="pagination")
  panel = pg.find("div", class_="row my-4")
  data = panel.find_all("div",class_="col-lg-4 col-md-6 mb-4")
  _scrape(data)
  for item in _getNexts(paginationNav=pagination):
    pg = Bs(get(url=host+path+item).text, "lxml")
    pagination = pg.find("ul", class_="pagination")
    panel = pg.find("div", class_="row my-4")
    data = panel.find_all("div", class_="col-lg-4 col-md-6 mb-4")
    _scrape(data)

def _pgnate(url):
  if url.strip() == "": return
  pg = Bs(get(url=url).text, "lxml")
  pagination = pg.find("ul", class_="pagination")
  panel = pg.find("div", class_="row my-4")
  data = panel.find_all("div", class_="col-lg-4 col-md-6 mb-4")
  _scrape(data)
  time.sleep(1.3)
  _pgnate(_getNext(paginationNav=pagination))


def paginate():
  _pgnate(url=host+path)
