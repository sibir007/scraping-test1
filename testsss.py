from urllib import parse
import requests, pickle
from lxml import html
from pathlib import Path
import util

# linc = 'https://zakupki.gov.ru/sInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'
# linc = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=%D1%83%D0%B7%D0%B5%D0%BB+%D1%83%D1%87%D1%91%D1%82%D0%B0&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'
# linc = 'https://google.com'
linc = 'https://zakupki.gov.ru'
headers_file = util.get_netloc(linc) + util.HEADERS_FILE
s = requests.Session()

cookies_file = Path(util.get_netloc(linc) + util.COOKIES_FIEL)

if not cookies_file.exists():
    with open(cookies_file, 'wb') as f:
        pickle.dump(s.cookies, f)
# if cookies_file.is_file():
with open(cookies_file, 'rb') as f:
    cookies_jar = pickle.load(f)

s.cookies = cookies_jar

s.headers = util.load_header_dict_from_json(headers_file)

r = s.get(linc)

print(r.status_code)
print('--------r.headers---------')
util.print_dict(r.headers)
print('--------r.headers.headers---------')
util.print_dict(r.request.headers)
print('--------s.cookies---------')
print(s.cookies)
print(r.cookies)
util.print_dict(s.cookies.get_dict())

r = s.get(linc)
print(r.status_code)
print('--------r.headers---------')
util.print_dict(r.headers)
print('--------r.headers.headers---------')
util.print_dict(r.request.headers)
print('--------s.cookies---------')
print(s.cookies)
print(r.cookies)
util.print_dict(s.cookies.get_dict())

# if cookies_file.is_file():
with open(cookies_file, 'r+b') as f:
    # cookies: dict = pickle.load(f)
    cookies_jar.update(s.cookies)
    pickle.dump(cookies_jar, f)

        
# request = s
