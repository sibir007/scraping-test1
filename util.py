from urllib import parse
import requests
from lxml import html
from contextlib import contextmanager
import pickle
import json
import os
from pathlib import Path
from requests import sessions
import lxml
import brotli

HEADERS_FILE_EXTENSION = '.headers.json'
COOKIES_FIEL_EXTENSION = '.cookies'
GENERAL_COOKIES_FILE_NAME = 'general' + COOKIES_FIEL_EXTENSION
UBUNTY_HEADERS_JSON_FILE = 'ubuntu_chromium_version_122.0.6261.128.headers.json'

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

@contextmanager
def session_cookies_manage(s: requests.Session):
    cookies = get_cookies_from_general_file()
    s.cookies = cookies
    yield s
    write_cookies_to_general_file(s.cookies)

def print_dict(d: dict, level: int = 0):
    shift = 4
    for k, v in d.items():
        print(level*4*' ' + f'{k}: {v}')
    

def print_unquoted_url(url: str):
    with pretty_print(print_unquoted_url):
        linc_unquot = parse.unquote_plus(url)
        print(linc_unquot)
    

def print_parsed_url(url: str):
    with pretty_print(print_parsed_url):
        linc_unquot = parse.unquote_plus(url)
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

def parse_raw_headers_from_file_to_dict_and_write_json_to_file(fname_from: str, fname_to: str = 'test-header.json'):
    """
    """
    h_dict = parse_raw_headers_to_dict(fname_from)
    write_header_dict_to_json(fname_to, h_dict)
                

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

def write_unquoted_link_in_file(link: str, fname: str = 'unqoted-lincs.txt'):
    """write unquoted link to file

    Args:
        link (str): linc to write
        fname (str, optional): file name. Defaults to 'unqoted-lincs.txt'.
       
    """
    unquoted_link = parse.unquote_plus(link)
    with open(fname, 'at') as f:
        f.write(unquoted_link)

def cookies_file_name_frome_link(link: str) -> str:
    """return cookies file name frome link

    Args:
        link (str): linck

    Returns:
        str: cookies file name
    """
    return get_netloc(link) + COOKIES_FIEL_EXTENSION
        
def get_cookies_from_file_named_based_on_link(link: str) -> sessions.RequestsCookieJar:
    """accept http link and forand based on it, RequestsCookieJar returns, 
    creates an empty one if necessary

    Args:
        link (str): link

    Returns:
        sessions.RequestsCookieJar: RequestsCookieJar
    """
    cookies_jar: sessions.RequestsCookieJar
    cookies_file = Path(cookies_file_name_frome_link(link))
    if not cookies_file.exists():
        with open(cookies_file, 'wb') as f:
            cookies_jar = sessions.cookiejar_from_dict({})
            pickle.dump(cookies_jar, f)
    else:        
        # if cookies_file.is_file():
        with open(cookies_file, 'rb') as f:
            cookies_jar = pickle.load(f)
    return cookies_jar

def get_cookies_from_general_file() -> sessions.RequestsCookieJar:
    """return RequestsCookieJar from general fale, 
    creates an empty one if necessary

    Returns:
        sessions.RequestsCookieJar: RequestsCookieJar
    """
    cookies_jar: sessions.RequestsCookieJar
    cookies_file = Path(GENERAL_COOKIES_FILE_NAME)
    if not cookies_file.exists():
        with open(cookies_file, 'wb') as f:
            cookies_jar = sessions.cookiejar_from_dict({})
            pickle.dump(cookies_jar, f)
    else:        
        # if cookies_file.is_file():
        with open(cookies_file, 'rb') as f:
            cookies_jar = pickle.load(f)
    return cookies_jar


def write_cookies_to_file_named_based_on_link(cookies: sessions.RequestsCookieJar, link: str):
    """write cookies jar to file named basen un link

    Args:
        cookies (sessions.RequestsCookieJar): RequestsCookieJar
        link (str) : link
    """
    with open(cookies_file_name_frome_link(link), 'wb') as f:
        pickle.dump(cookies, f)
    
def write_cookies_to_general_file(cookies: sessions.RequestsCookieJar):
    """write cookies jar to general file

    Args:
        cookies (sessions.RequestsCookieJar): RequestsCookieJar
    """
    with open(GENERAL_COOKIES_FILE_NAME, 'wb') as f:
        pickle.dump(cookies, f)
    
def write_content_to_file(link: str, fname: str):
    """accept link and write content to file by name

    Args:
        link (str): link to download content
        fname (str): file name for write
    """
    session = requests.Session()
    session.headers = load_header_dict_from_json(UBUNTY_HEADERS_JSON_FILE)
    with session_cookies_manage(session) as s:
        with open(fname, 'wb') as f:
            f.write(s.get(link).content)
            # s.request.


def decompress_brotli_from_file_to_file(fname_from: str, fname_to):
    with open(fname_from, 'rb') as fr:
        with open(fname_to, 'wb') as fw:
            fw.write(brotli.decompress(fr.read()))

# write_content_to_file('https://www.maketecheasier.com/cheatsheet/vscode-keyboard-shortcuts/','shortcuts.br')
# decompress_brotli_from_file_to_file('shortcuts.br', 'shortcuts.html')
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
############# Комплексный тэст куков начало ####################
# searchString1 = parse.quote_plus('приборы учёта')
# searchString2 = parse.quote_plus('мёд')
# link1_for_tests = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={searchString}&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'
# link2_for_tests = 'https://www.google.com/search?q={searchString}_esv=89d0d0f18241ff13&sca_upv=1&sxsrf=ACQVn08QHyY43yl6Is7CiDQ-sB8SLO-0WQ%3A1713012968153&ei=6IAaZs2CCZmMwPAPoMawwAQ&udm=&ved=0ahUKEwjNltnLnr-FAxUZBhAIHSAjDEgQ4dUDCBA&uact=5&oq=cookies&gs_lp=Egxnd3Mtd2l6LXNlcnAiB2Nvb2tpZXMyDhAuGIAEGMcBGK8BGI4FMggQABiABBixAzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMh0QLhiABBjHARivARiOBRiXBRjcBBjeBBjgBNgBAkihdlAAWIBfcAd4AZABAJgBoQGgAb0MqgEEMC4xM7gBA8gBAPgBAZgCFKACkw-oAhDCAgcQIxjqAhgnwgIWEC4YgAQYigUYQxjIAxjqAhi0AtgBAcICGRAuGIAEGIoFGEMY1AIYyAMY6gIYtALYAQHCAgoQIxiABBiKBRgnwgILEAAYgAQYsQMYgwHCAgsQLhiABBjHARjRA8ICBRAuGIAEwgIEECMYJ8ICCxAuGIAEGLEDGIMBwgILEAAYgAQYigUYsQPCAg4QLhiABBixAxjHARjRA8ICERAuGIAEGLEDGIMBGMcBGNEDwgIOEAAYgAQYigUYsQMYgwHCAgsQLhiABBjHARivAcICEBAuGIAEGAoYxwEYrwEYjgXCAgcQABiABBgKwgIREC4YgAQYxwEYrwEYmAUYmQXCAg0QLhiABBgKGMcBGNEDwgIKEAAYgAQYChixA8ICDRAuGIAEGAoYxwEYrwHCAh8QLhiABBgKGMcBGK8BGI4FGJcFGNwEGN4EGOAE2AECwgIIEC4YsQMYgATCAg0QABiABBixAxhGGP8BwgIIEC4YgAQYsQPCAiQQABiABBixAxhGGP8BGJcFGIwFGN0EGEYY_wEY9AMY9QPYAQPCAgsQLhiABBixAxjUAsICGhAuGIAEGLEDGIMBGJcFGNwEGN4EGOAE2AECmAMMugYGCAEQARgIugYGCAIQARgUugYGCAMQARgTkgcENy4xM6AH3rUB&sclient=gws-wiz-serp'

# s = sessions.Session()
# s.headers = load_header_dict_from_json(UBUNTY_HEADERS_JSON_FILE)
# s.cookies = get_cookies_from_general_file()

# print_dict(s.cookies.get_dict())

# resp = s.get(link1_for_tests.format(searchString=searchString1))
# print('respons1 status code: ', resp.status_code)
# print('response1 cookies header', resp.request.headers.get('Cookie', 'non seted'), sep=': ')
# print_dict(s.cookies.get_dict())
# resp = s.get(link1_for_tests.format(searchString=searchString2))
# print('respons2 status code: ', resp.status_code)
# print('response2 cookies header', resp.request.headers.get('Cookie', 'non seted'), sep=': ')
# print_dict(s.cookies.get_dict())

# resp = s.get(link2_for_tests.format(searchString=searchString1))
# print('respons3 status code: ', resp.status_code)
# print('response3 cookies header', resp.request.headers.get('Cookie', 'non seted'), sep=': ')
# print_dict(s.cookies.get_dict())
# resp = s.get(link2_for_tests.format(searchString=searchString2))
# print('respons4 status code: ', resp.status_code)
# print('response4 cookies header', resp.request.headers.get('Cookie', 'non seted'), sep=': ')
# print_dict(s.cookies.get_dict())

# write_cookies_to_general_file(s.cookies)
# cookies = get_cookies_from_general_file()
# print_dict(cookies.get_dict())

# for item in get_cookies_from_file_named_based_on_link('zakupki.gov.ru.cookies'):
#     print(item)
############# Комплексный тэст куков окончание ####################
# # # parse

############## тест пагинатрорв начало #########################

def _test_pagginator():
    link1_for_tests = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={searchString}&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={pageNumber}&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'.format(searchString=parse.quote_plus('приборы учёта'), pageNumber='1')

    xpat_paginators = '//div[contains(@class, "paginator")]'
    xpat_pagenumbers = '//a[@data-pagenumber]/@data-pagenumber'

    s = requests.Session()
    s.headers = load_header_dict_from_json(UBUNTY_HEADERS_JSON_FILE)
    with session_cookies_manage(s) as s:
        zakup_html = s.get(link1_for_tests).text
    # with open('zakup.html', 'rt') as f:
    #     zakup_html = f.read()    
        
    zak_el = html.fromstring(zakup_html)
    paginator_el: lxml.html.HtmlElement = zak_el.xpath(xpat_paginators)[0]
    print(paginator_el[0].get('class'))
    page_numbers = paginator_el.xpath(xpat_pagenumbers)
    for num in page_numbers:
        print(num)    
# pagenumbers = paginator_el.xpath(xpat_pagenumbers)
# for pahe_numb in pagenumbers:
# print(pahe_numb)
# while next_page <= total_pages:
#     # if next_page == 1:
      

# _test_pagginator()

############## тест пагинатрорв окончание #########################

def test_quoting():
    search_link = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={searchString}&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={pageNumber}&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'
    search_link_unquoted = parse.unquote_plus(search_link)
    print(search_link_unquoted)
    print(parse.quote(search_link_unquoted))
    'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={searchString}&morphology=on&search-filter=Дате размещения&pageNumber={pageNumber}&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'

# write_headers_frome_file_to_file_as_dict('windows-chrome-headers.txt', 'windows-chrome-headers.txt')
# parse_raw_headers_to_dict('windows-chrome-headers.txt')
# parse_raw_headers_from_file_to_dict_and_write_json_to_file('windows-chrome-headers.txt', 'windows-chrome-headers.json')
                    # # НАЧАЛО----------------------- Работа с query --------------------------------
                    # link2 =          'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=%D1%83%D0%B7%D0%B5%D0%BB+%D1%83%D1%87%D1%91%D1%82%D0%B0&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'
                    # link2_unquoted = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=узел учёта&morphology=on&search-filter=Дате размещения&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'
                    # linc2_quoted_plus = 'https%3A%2F%2Fzakupki.gov.ru%2Fepz%2Forder%2Fextendedsearch%2Fresults.html%3FsearchString%3D%D1%83%D0%B7%D0%B5%D0%BB+%D1%83%D1%87%D1%91%D1%82%D0%B0%26morphology%3Don%26search-filter%3D%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F%26pageNumber%3D1%26sortDirection%3Dfalse%26recordsPerPage%3D_10%26showLotsInfoHidden%3Dfalse%26sortBy%3DUPDATE_DATE%26fz44%3Don%26fz223%3Don%26af%3Don%26ca%3Don%26pc%3Don%26pa%3Don%26currencyIdGeneral%3D-1'
                    # link2_parsed = parse.urlparse(link2)
                    # link2_query = link2_parsed.query
                    # link2_query_unquoted = parse.unquote_plus(link2_query)
                    # link2_query_unquoted_parsed = parse.parse_qs(link2_query_unquoted)
                    # print_dict(link2_query_unquoted_parsed)
                    # link2_query_unquoted_parsed_back = parse.urlencode(link2_query_unquoted_parsed, doseq=True)
                    # print()
                    # print(link2_query_unquoted_parsed_back)
                    # print()

                    # link2_back = link2_parsed._replace(query=link2_query_unquoted_parsed_back).geturl()
                    # print(link2_back)
                    # print(link2==link2_back)

                    # # КОНЕЦ----------------------- Работа с query --------------------------------
# = parse.quote_plus(link2_unquoted)
# print(linc2_quoted)