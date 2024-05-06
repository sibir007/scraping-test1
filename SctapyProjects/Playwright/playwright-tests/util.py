from playwright.sync_api import sync_playwright, Browser, Page, Request, Response
from typing import Mapping, Tuple, List, Sequence, Union, Any
from urllib import parse
from lxml import html
from contextlib import contextmanager
import pickle
import json
import os
from pathlib import Path
import lxml
import brotli
import shutil
import pydlib as dl


VZLJOT_PROXY = {
  'http': 'http://SibiryakovDO:vzlsoFia1302@proxy:3128',
  'https': 'http://SibiryakovDO:vzlsoFia1302@proxy:3128',
}
NEW_PYBLIC_LINK = 'https://torgi.gov.ru/new/public'
NEW_PYBLIC_LOTS_REG_LINK = 'https://torgi.gov.ru/new/public/lots/reg'
HEADERS_DIR = 'headers/'
HEADERS_FILE_EXTENSION = '.headers.json'
COOKIES_DIR = 'coodies/'
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

# def parse_raw_headers_from_file_to_dict_and_write_json_to_file(fname_from: str, fname_to: str = 'test-header.json'):
#     """
#     """
#     h_dict = parse_raw_headers_to_dict(fname_from)
#     write_header_dict_to_json_file(fname_to, h_dict)
                

def get_netloc(linc: str) -> str:
    """return netloc frome linc string

    Args:
        linc (str): linc, url

    Returns:
        str: netloc
    """
    parse_linc = parse.urlparse(linc)
    return parse_linc.netloc

        
        
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

def load_header_dict_from_json_file(fname: str) -> dict:
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

def write_header_dect_to_file(hdict: dict, fname: str = 'test'):
    """write headers in dict to file

    Args:
        hdict (dict): dect headers
        fname (str, optional): file name. Defaults to 'test'.
    """
    with open(f'{fname}.headers', 'wb') as f:
        pickle.dump(hdict, f)


def write_dict_or_list_to_json_file(fname: str, obj: Union[List, Mapping]):
    """load to json file header dict

    Args:
        fname (str): file name
        hdict (dict): header dict
    """
    with open(fname, 'wt', encoding='utf-8') as f:
        json_str = json.dumps(obj, indent=4, ensure_ascii=False)
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




def decompress_brotli_from_file_to_file(fname_from: str, fname_to):
    with open(fname_from, 'rb') as fr:
        with open(fname_to, 'wb') as fw:
            fw.write(brotli.decompress(fr.read()))

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


def get_request_response_headers(link: str, browser: str = 'firefox') -> Tuple[Mapping[str, str], Mapping[str, str]]:
    """accept link return tuple response request headers dicts

    Args:
        link (str): link
        browser (str): browser type 
    Returns:
        Tuple[Mapping[str, str], Mapping[str, str]]: tuple reqvest response headers dict
    """
    resp_headers: Mapping[str, str]
    req_headers: Mapping[str, str]
    # cookies: 
    with sync_playwright() as p:
        # p.chromium.launch(headless=False, slow_mo=50)
        browser_impl: Browser = getattr(p, browser).launch(headless=False, slow_mo=50)
        page: Page = browser_impl.new_page()
        
        response: Response = page.goto(link)
        resp_headers = response.all_headers()
        req_headers = response.request.all_headers()
        browser_impl.close()
        

    return req_headers, resp_headers

# for d in get_request_response_headers(NEW_PYBLIC_LOTS_REG_LINK):
#      print_dict(d)
# # print()
def _get_request_json_response_dicts_dict_calback(result: list):
    # result_list = result
    def request_json_response_dicts_list_calback(request: Request):
        response: Response = request.response()
        if response.header_value('content-type') == 'application/json':
            result_dict = {}
            result_dict['request_url'] = request.url
            result_dict['request_headers'] = request.all_headers()
            result_dict['response_headers'] = response.all_headers()
            result_dict['response_json'] = response.json()
            # req_url = request.url
            # resp_json = request.response().json()
            result.append(result_dict)
        # pass
    return request_json_response_dicts_list_calback
        
def get_request_json_response_dicts_list(linc: str, browser: str = 'firefox') -> Sequence[Mapping]:
    result: list = []
    with sync_playwright() as p:
        browser_impl: Browser = getattr(p, browser).launch(headless=False, slow_mo=50)
        page: Page = browser_impl.new_page()
        page.on('requestfinished', _get_request_json_response_dicts_dict_calback(result))
        page.goto(linc)
        browser_impl.close()
    return result


def _get_request_json_response_dicts_dict_calback(result: dict):
    # result_dict = result
    def request_json_response_dicts_dict_calback(request: Request):
        response: Response = request.response()
        if response.header_value('content-type') == 'application/json':
            result_dict = {}
            request_url = request.url
            result_dict['request_url'] = request_url
            result_dict['request_headers'] = request.all_headers()
            result_dict['response_headers'] = response.all_headers()
            result_dict['response_json'] = response.json()
            # req_url = request.url
            # resp_json = request.response().json()
            result[request_url] = result_dict
        # pass
    return request_json_response_dicts_dict_calback

def get_request_json_response_dicts_dict(linc: str, browser: str = 'firefox') -> Mapping[str, Mapping]:
    result: dict = {}
    with sync_playwright() as p:
        browser_impl: Browser = getattr(p, browser).launch(headless=False, slow_mo=50)
        page: Page = browser_impl.new_page()
        page.on('requestfinished', _get_request_json_response_dicts_dict_calback(result))
        page.goto(linc)
        browser_impl.close()
    return result



# TODO: implement
def _get_ownership_form_list__check_version(request_info2_data: dict, fun_version: str) -> bool:
    """проверка соответствии версии функции get_ownership_form_list(fname: str) 
    и версии апи указанной в request_info2.json  файле. Печатае результа в stdout

    Args:
        request_info2_data (dict): request_info2.json dict
        fun_version (str): version get_ownership_form_list()
    Returns:
        Union[True, False]: True or False for caler fun
    """
    return True

def get_ownership(fname: str, return_value: str = 'list') -> Union[List[str], Mapping[str, str]]:
    """accept request_info2.json file format and type return value, 
    return list ownership code or dict ownership_code:ownership_name 

    Args:
        fname (str): json file format request_info2.json
        return_value (str) 'list' or 'dict', defaul 'list': return value list [ownership_code] or dict {ownership_code:ownership_name}
    Returns:
        Union[List[str], Mapping[str, str]]: list [ownership_code] or dict {ownership_code:ownership_name}
    """
    #version torgi.gov.ru for check
    # version_api = '3.1'
    # ownershp_code_list: list[str]
    # with open(fname, 'rb') as f:
    #     data_json = f.read()
    #     # try
    #     data_dict = json.loads(data_json)
        # # TODO: обработать вызов
        # _get_ownership_form_list__check_version(data_dict, version_api)
        # ownershp_dict_list: list[dict] = data_dict['https://torgi.gov.ru/new/nsi/v1/OWNERSHIP_FORM']['response_json']
        # if return_value == 'dict':
        #     ownershp_result: dict[str, str] = {ownershp_dict['code']: ownershp_dict['name'] for ownershp_dict in ownershp_dict_list}
        # else:
        #     ownershp_result: list[str] = [ownershp_dict['code'] for ownershp_dict in ownershp_dict_list]
    return get_relationship(fname=fname, 
                            url='https://torgi.gov.ru/new/nsi/v1/OWNERSHIP_FORM', 
                            code='code',
                            value='name',
                            return_value=return_value)


def get_relationship(fname: str, url: str, code: str, value: str, return_value: str = 'list') -> Union[List[str], Mapping[str, str]]:
    """accept request_info2.json file format, url, code str, value str and type return value, 
    return list relationship code or dict relationship_code:relationship_name 
    url['response_json'] obgect must be form [{code: some_code_value, value:some_value_value, ...}, {}, {}]

    Args:
        fname (str): json file format request_info2.json
        url (str): url str for search in file
        code (str): code str
        value (str): value str
        return_value (str) 'list' or 'dict', defaul 'list': return value list [some_code_value, ...] or dict {some_code_value:some_value_value, ...}
    Returns:
        Union[List[str], Mapping[str, str]]: list [some_code_value, some_code_value, ...] or dict {some_code_value:some_value_value, some_code_value:some_value_value, ...}
    """
    #version torgi.gov.ru for check
    version_api = '3.1'
    # ownershp_code_list: list[str]
    with open(fname, 'rb') as f:
        data_json = f.read()
        # try
        data_dict = json.loads(data_json)
        
        # TODO: обработать вызов
        _get_ownership_form_list__check_version(data_dict, version_api)
        
        
        
        relationship_dict_list: list[dict] = data_dict[url]['response_json']
        if return_value == 'dict':
            relationship_result: dict[str, str] = {relationship_dict[code]: relationship_dict[value] for relationship_dict in relationship_dict_list}
        else:
            relationship_result: list[str] = [relationship_dict[code] for relationship_dict in relationship_dict_list]
    return relationship_result

def get_relationship_v2(info2_fname: str, 
                        code_path: str, 
                        code_key: str, 
                        value_path: str, 
                        value_key: str,
                        ) -> Mapping[str, str]:
    """accept request_info2.json file format, code_path, code_key, value_path, value_key
    and type return value, return dict {code:value, ...} 

    Args:
        info2_fname (str): json file format request_info2.json
        code_path (str): path to code dict, forma: a`b`c
        code_key (str):  code key
        value_path (str): path to value dict, forma: a`b`c
        value_key (str):  value key
    Returns:
        Mapping[str, str]: dict {some_code_value:some_value_value, some_code_value:some_value_value, ...}
    """
    #version torgi.gov.ru for check
    version_api = '3.1'
    # ownershp_code_list: list[str]
    with open(info2_fname, 'rb') as f:
        data_json = f.read()
        # try
        data_dict = json.loads(data_json)
        
    # TODO: обработать вызов
    _get_ownership_form_list__check_version(data_dict, version_api)
    
    
    
    key_list: list[Any] = dl.get(data_dict, code_path + '`' + code_key, sep='`')
    value_list: list[Any] =   dl.get(data_dict, value_path + '`' + value_key, sep='`')
 
    key_value_zip = zip(key_list, value_list)    
    # if return_value == 'dict':
    key_value_dict: dict[str, str] = {key: value for key, value in key_value_zip}
        # else:
            # relationship_result: list[str] = [relationship_dict[code_path] for relationship_dict in relationship_dict_list]
    return key_value_dict

def _get_key_valu_dicts(code_path, value_path, relationship_dict_list):
    for d in relationship_dict_list:
        target_relationship_key_dict: dict = d
        for key in code_path:
            if not (target_relationship_key_dict := target_relationship_key_dict.get(key, {})):
                break
        if not target_relationship_key_dict:
            continue
        target_relationship_value_dict: dict = d
        for key in value_path:
            if not (target_relationship_value_dict := target_relationship_value_dict.get(key, {})):
                break
        if not target_relationship_value_dict:
            continue
        yield target_relationship_key_dict, target_relationship_value_dict
    #     target_relationship_key_dict_list.append(target_relationship_key_dict)
    #     target_relationship_value_dict_list.append(target_relationship_value_dict)
    #     zip_dict_lists = zip(target_relationship_key_dict_list, target_relationship_value_dict_list)
    # return zip_dict_lists



def write_value_to_dict_in_json_file(fname: str, target_dict_paths: List[str], key_for_insert: str, value_for_insert: Union[list, dict]):
    """принимает json файл, путь и значение для вставки в json
    если target_dict_paths не существуе - создаёт его

    Args:
        fname (str): json file name
        target_dict_paths (List[str]): list string to dict
        key_for_insert (str): key name for insert value
        value_for_insert (Union[str, dict]): list or dict for inserting
    """
    
    with open(fname, 'r+', encoding='utf-8') as f:
        loaded_dict: dict = json.loads(f.read())
        target_dict: dict = loaded_dict
        
        # target: Union[List, Mapping]
        for path in target_dict_paths:
            if not path in target_dict.keys():
                target_dict[path] = {}
            target_dict = target_dict[path]
        target_dict[key_for_insert] = value_for_insert
        json_str = json.dumps(loaded_dict, indent=4, ensure_ascii=False)
        f.seek(0)
        f.write(json_str)


def write_value_to_dict_in_json_file_v2(fname: str, path: str, value: Any):
    """принимает json файл, путь и значение для вставки в json
    если target_dict_paths не существуе - создаёт его

    Args:
        fname (str): json file name
        paths (str): path to dict: a`b`c`d
        value_for_insert (Any): Amy valu for inserting
    """
    
    with open(fname, 'r+', encoding='utf-8') as f:
        loaded_dict: dict = json.loads(f.read())
        # target_dict: dict = loaded_dict
        
        # target: Union[List, Mapping]
        # for path in target_dict_paths:
        #     if not path in target_dict.keys():
        #         target_dict[path] = {}
        #     target_dict = target_dict[path]
        # target_dict[key_for_insert] = value_for_insert
        loaded_dict = dl.update(loaded_dict, path, value, sep='`')
        json_str = json.dumps(loaded_dict, indent=4, ensure_ascii=False)
        f.seek(0)
        f.write(json_str)
    
    
# "request_url": "https://torgi.gov.ru/new/nsi/v1/RELATIONSHIP_BIDD_HINTEXT",

# print(json.dumps(get_relationship('request_info2.json', url='https://torgi.gov.ru/new/nsi/v1/RELATIONSHIP_BIDD_HINTEXT', code='code', value='fullName', return_value='list'), ensure_ascii=False))
# print(json.dumps(get_relationship('request_info2.json', url='https://torgi.gov.ru/new/nsi/v1/RELATIONSHIP_BIDD_HINTEXT', code='code', value='fullName', return_value='dict'), ensure_ascii=False))

FORM_FIELDS = [
    'Поисковый запрос',
    'Нормативный правовой акт',
    'Вид торгов',
    'Вид сделки',
    'Форма проведения торгов',
    'Субъект местонахождения имущества',
    'Местонахождение имущества',
    'Категория',
               ]

def form_field_Нормативный_правовой_акт():
    url = 'https://torgi.gov.ru/new/nsi/v1/RELATIONSHIP_BIDD_HINTEXT'
    t_path = ['form', 'Нормативный правовой акт']
    a_key = 'available_values'
    a_value = get_relationship('request_info2.json', url=url, code='code', value='fullName', return_value='list')
    a_h_key = 'available_values_hint'
    a_h_value = get_relationship('request_info2.json', url=url, code='code', value='fullName', return_value='dict')
    write_value_to_dict_in_json_file(
        'search_form.json',
        t_path, 
        a_key,
        a_value
        )
    write_value_to_dict_in_json_file(
        'search_form.json',
        t_path, 
        a_h_key,
        a_h_value
        )
    
def form_field(searsh_form_file: str, form_field_name: str, info2_file_name:str):
    # with open(info2_file_name) as info2_f:
    # резервная копия
    shutil.copy(searsh_form_file, 'copy.'+searsh_form_file)
    with open(searsh_form_file, encoding='utf-8') as form_file:
        form_dict = json.loads(form_file.read())
        url_key = form_dict['form'][form_field_name]['info2_url']
        aviavailable_values_key = form_dict['form'][form_field_name]['available_values']['key']
        aviavailable_values_hint_key = form_dict['form'][form_field_name]['available_values_hint']['key']
        aviavailable_values_hint_value = form_dict['form'][form_field_name]['available_values_hint']['value']

    v_t_path = ['form', form_field_name, 'available_values']
    v_h_t_path = ['form', form_field_name, 'available_values_hint']
    a_key = 'values'
    a_h_key = 'values'

    a_value = get_relationship(info2_file_name, url=url_key, code=aviavailable_values_key, value=aviavailable_values_hint_value, return_value='list')
    a_h_value = get_relationship(info2_file_name, url=url_key, code=aviavailable_values_hint_key, value=aviavailable_values_hint_value, return_value='dict')
    write_value_to_dict_in_json_file(
        searsh_form_file,
        v_t_path, 
        a_key,
        a_value
        )
    write_value_to_dict_in_json_file(
        searsh_form_file,
        v_h_t_path, 
        a_h_key,
        a_h_value
        )

def form_field_v2(searsh_form_file: str, form_field_name: str, info2_file_name:str):
    # with open(info2_file_name) as info2_f:
    # резервная копия
    shutil.copy(searsh_form_file, 'copy.'+searsh_form_file)
    with open(searsh_form_file, encoding='utf-8') as form_file:
        form_dict: dict = json.loads(form_file.read())
    url_key = dl.get(form_dict, f'form`{form_field_name}`info2_url', sep='`')
    # url_key = form_dict['form'][form_field_name]['info2_url']
    aviavailable_values_path = dl.get(form_dict, f'form`{form_field_name}`available_values`path', sep='`')
    # aviavailable_values_path = form_dict['form'][form_field_name]['available_values']['key']
    aviavailable_values_hint_path = dl.get(form_dict, f'form`{form_field_name}`available_values_hint`path', sep='`')
    # aviavailable_values_hint_path = form_dict['form'][form_field_name]['available_values_hint']['key']
    full_a_v_path = f'{url_key}`{aviavailable_values_path}'
    # v_t_path = ['form', form_field_name, 'available_values']
    full_a_v_h_path = f'{url_key}`{aviavailable_values_hint_path}'
    # v_h_t_path = ['form', form_field_name, 'available_values_hint']
    # aviavailable_values_hint_value = form_dict['form'][form_field_name]['available_values_hint']['value']
    aviavailable_values_key = dl.get(form_dict, f'form`{form_field_name}`available_values`key', sep='`')
    # aviavailable_values_key = 'values'
    aviavailable_values_hint_key = dl.get(form_dict, f'form`{form_field_name}`available_values_hint`key', sep='`')


    res: Mapping[str, str] = get_relationship_v2(info2_file_name, 
                                  code_path=full_a_v_path, 
                                  code_key=aviavailable_values_key,
                                  value_path=full_a_v_h_path, 
                                  value_key=aviavailable_values_hint_key)

    # a_h_value = get_relationship_v2(info2_file_name, url=url_key, code=aviavailable_values_hint_path, value=aviavailable_values_hint_value, return_value='dict')
    # keys = 
    form_aviavailable_values_path = f'form`{form_field_name}`available_values`values'
    form_aviavailable_values_hint_path = f'form`{form_field_name}`available_values_hint`values'
    write_value_to_dict_in_json_file_v2(
        searsh_form_file,
        form_aviavailable_values_hint_path,
        res
        )
    write_value_to_dict_in_json_file_v2(
        searsh_form_file,
        form_aviavailable_values_path, 
        list(res.keys())
        )



    
if __name__ == '__main__':
    # res = get_request_json_response_dicts_dict(NEW_PYBLIC_LOTS_REG_LINK)
    # write_dict_or_list_to_json_file('win.06.05.24.request_info2.json', res)
    # form_field('search_form.json', 'Вид сделки', 'request_info2.json')
    form_field_v2('search_form.v2.json', 'Форма проведения торгов', 'request_info2.json')