import requests
import re
import lxml
import csv
import util

sourceUrl = 'http://quotes.toscrape.com/'
keys = ['quote_tags', 'autor_url', 'author_name', 'born_date', 'born_location', 'quote_title']
session = requests.Session()
session.headers = util.load_header_dict_from_json(U)