import requests
from bs4 import BeautifulSoup

class WrongNum(Exception):
  pass


def currency_converter(amount, source, target):
  url ="https://wise.com/gb/currency-converter/"
  query = f"{source}-to-{target}-rate?amount={amount}"

  webpage = requests.get(url+query)
  soup = BeautifulSoup(webpage.text, "html.parser")
  try:
    calc = soup.find("div", {"class": "js-Calculator"})
    rate = calc.find("span", {"class": "text-success"})
  except AttributeError:
    return False
  rate = rate.string
  result = float(rate) * amount
  return result


### Job Finding ###

def extract_indeed_pages(url):
    indeed_result = requests.get(url)
    indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

    pagination = indeed_soup.find("div",attrs={"class":"pagination"})
    pages = pagination.find_all('a')

    spans = []
    for page in pages[:-1]:
      spans.append(page.find("span"))

    pn = []
    for page in pages[:-1]:
      pn.append(int(page.string))
    max_page = pn[-1]

    return max_page

def extract_indeed_jobs(url, last_page, limit):
    jobs = []

    for page in range(last_page):
        result = requests.get(f"{url}&start={page*limit}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            title = result.find("h2", {"class": "title"})
            anchor = title.find("a")["title"]
            print(anchor)

    return jobs