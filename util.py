from urllib import parse
import requests
from lxml import html
from contextlib import contextmanager
import pickle
import json
import os

HEADERS_FILE = '.headers.json'
COOKIES_FIEL = '.cookies'

VZLJOT_PROXY = {
  'http': 'http://SibiryakovDO:vzlsOfia1302@proxy:3128',
  'https': 'http://SibiryakovDO:vzlsOfia1302@proxy:3128',
}



url_parts = ('scheme', 'netloc', 'path', 'params', 'query', 'fragment')
linc = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=%D1%83%D0%B7%D0%B5%D0%BB+%D1%83%D1%87%D1%91%D1%82%D0%B0&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'

@contextmanager
def pretty_print(fun_name: callable):
    print(f'----------{fun_name.__name__}----------')
    yield
    print('-------------------------------')


def print_dict(d: dict, level: int = 0):
    shift = 4
    for k, v in d.items():
        print(level*4*' ' + f'{k}: {v}')
    

def print_unquoted_url(url: str):
    with pretty_print(print_unquoted_url):
        linc_unquot = parse.unquote_plus(linc)
        print(linc_unquot)
    

def print_parsed_url(url: str):
    with pretty_print(print_parsed_url):
        linc_unquot = parse.unquote_plus(linc)
        linc_parsed = parse.urlparse(linc_unquot)
        linc_parsed_dict = linc_parsed._asdict()
        query_str = linc_parsed_dict['query']
        del linc_parsed_dict['query']
        query_dict = parse.parse_qs(query_str)
        print_dict(linc_parsed_dict)
        print('query - ')
        print_dict(query_dict, level=1)



def parse_raw_headers_to_dict(file: str) -> dict:
    header_dict = {}
    with open(file, 'rt') as f:
        for line in f:
            ind = line.find(':')
            head, tail = line[:ind], line[ind+1:]
            header_dict[head.strip()] = tail.strip()
    return header_dict
            

def get_netloc(linc: str) -> str:
    """return netloc frome linc string

    Args:
        linc (str): linc, url

    Returns:
        str: netloc
    """
    parse_linc = parse.urlparse(linc)
    return parse_linc.netloc

def write_header_dect_to_file(hdict: dict, fname: str = 'test'):
    """write headers in dict to file

    Args:
        hdict (dict): dect headers
        fname (str, optional): file name. Defaults to 'test'.
    """
    with open(f'{fname}.headers', 'wb') as f:
        pickle.dump(hdict, f)
def write_headers_frome_file_to_file_as_dict(hfile: str, fname: str = 'test'):
    hdict = parse_raw_headers_to_dict(hfile)
    write_header_dect_to_file(hdict=hdict, fname=fname)
   
   
def load_header_dict(fname: str) -> dict:
    """load from file header dict

    Args:
        fname (str): file name

    Returns:
        dict: header dict
    """
    with open(fname, 'rb') as f:
        hdict = pickle.load(f)
    return hdict

def load_header_dict_from_json(fname: str) -> dict:
    """load from json file header dict

    Args:
        fname (str): file name

    Returns:
        dict: header dict
    """
    with open(fname, 'rt') as f:
        data = f.read()
        hdict = json.loads(data)
    return hdict

def write_header_dict_to_json(fname: str, hdict: dict):
    """load to json file header dict

    Args:
        fname (str): file name
        hdict (dict): header dict
    """
    with open(fname, 'wt') as f:
        json_str = json.dumps(hdict, indent=4)
        f.write(json_str)



# hdict = load_header_dict('test2.headers')       
# print_dict(hdict)
# write_headers_frome_file_to_file_as_dict('tests_copy2.txt', fname='test2')
# header_dict = parse_raw_headers_to_dict('tests_copy.txt')
# print_dict(header_dict)
# write_header_dict_to_json('test.header.json', header_dict)            
# print_unquoted_url(url_parts)
# print_parsed_url(linc)
# hdict = load_header_dict_from_json('test.header.json')
# print_dict(hdict)
# linc_parsed = parse.urlparse(linc_unquot)
# print_dict(linc_parsed._asdict(), dict_name='linc_parsed')

    
# query_part = linc_parsed.query

# query_part_parsed = parse.parse_qs(query_part)

# print_dict(query_part_parsed, dict_name='query_part_parsed')


# s = requests.Session()
# resp = s.get(linc)

# netloc = get_netloc('https://google.com')
# print(netloc)
# print(resp.status_code) 

# print_dict(resp.headers, 'response')
# print_dict(resp.request.headers, 'request')

# # print_dict(s.cookies, 'cookies')
# for c,v in s.cookies.items():
#     print(f'{c} -- {v}')

# print_dict(os.environ)
# # parse

