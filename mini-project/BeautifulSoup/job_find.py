import requests
from bs4 import BeautifulSoup
import configparser
import pathlib

from lib import extract_indeed_pages, extract_indeed_jobs

config = configparser.ConfigParser()
dir = pathlib.PurePath(__file__).parent
url = "https://www.indeed.com/jobs?q=python&limit=50"
limit = 50



if pathlib.Path(f'{dir}\config.ini').exists():
    config.read(f'{dir}\config.ini')
    max_page = int(config['indeed.com']['max_page'])
else:
    max_page = extract_indeed_pages(url)
    config['indeed.com'] = {}
    config['indeed.com']['max_page'] = str(max_page)
    with open(f'{dir}\config.ini', 'w') as f:
        config.write(f)

jobs = extract_indeed_jobs(url, max_page, limit)
