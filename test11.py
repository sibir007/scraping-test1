from urllib import parse
import requests, pickle
from lxml import html


linc = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=%D1%83%D0%B7%D0%B5%D0%BB+%D1%83%D1%87%D1%91%D1%82%D0%B0&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'


def get_netloc(linc: str) -> str:
    parse_linc = parse.urlparse(linc)
    return parse_linc.netloc

s = requests.Session()
with open(f'{get_netloc(linc)}.cookies', 'rb') as f:
    cookies = pickle.loads(f)


resp = s.get(linc)



print(resp.status_code) 



# parse

