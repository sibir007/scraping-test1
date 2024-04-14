from urllib import parse
import sys
import urllib.parse
import lxml.html
from time import gmtime, strftime
import json
# import lxml.html
# from lxml.html import HtmlElement
# from html import H
# import lxml.html
import util
import urllib
import requests
import os
import lxml
link1 = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=%D1%83%D1%87%D1%91%D1%82&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'
link2 = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=%D1%83%D1%87%D1%91%D1%82&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D0%BE%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=100&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&savedSearchSettingsIdHidden=&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&placingWayList=&selectedLaws=&priceFromGeneral=&priceFromGWS=&priceFromUnitGWS=&priceToGeneral=&priceToGWS=&priceToUnitGWS=&currencyIdGeneral=-1&publishDateFrom=&publishDateTo=&applSubmissionCloseDateFrom=&applSubmissionCloseDateTo=&customerIdOrg=&customerFz94id=&customerTitle=&okpd2Ids=&okpd2IdsCodes='
link3 = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=%D1%83%D1%87%D1%91%D1%82&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D0%BE%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&savedSearchSettingsIdHidden=&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&placingWayList=&selectedLaws=&priceFromGeneral=&priceFromGWS=&priceFromUnitGWS=&priceToGeneral=&priceToGWS=&priceToUnitGWS=&currencyIdGeneral=-1&publishDateFrom=&publishDateTo=&applSubmissionCloseDateFrom=&applSubmissionCloseDateTo=&customerIdOrg=&customerFz94id=&customerTitle=&okpd2Ids=&okpd2IdsCodes='
link3_unquoted = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={searchString}&morphology=on&search-filter={search-filter}&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&savedSearchSettingsIdHidden=&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&placingWayList=&selectedLaws=&priceFromGeneral=&priceFromGWS=&priceFromUnitGWS=&priceToGeneral=&priceToGWS=&priceToUnitGWS=&currencyIdGeneral=-1&publishDateFrom=&publishDateTo=&applSubmissionCloseDateFrom=&applSubmissionCloseDateTo=&customerIdOrg=&customerFz94id=&customerTitle=&okpd2Ids=&okpd2IdsCodes='
# link3_unquoted = urllib.parse.unquote_plus(link3)
# print(link3_unquoted)

searchString1 = parse.quote_plus('приборы учёта')
# searchString2 = parse.quote_plus('мёд')
link1_for_tests = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={searchString}&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={pageNumber}&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'.format(searchString=parse.quote_plus('учёта'), pageNumber='1')


# xpat_paginators = '//div[contains(@class, "paginator")]'
# xpat_pagenumbers = '//a[@data-pagenumber]/@data-pagenumber'




def prepare_scrapping():
  pass
  # for pahe_numb in pagenumbers:
  #   print(pahe_numb)
  # while next_page <= total_pages:
  #   if next_page == 1:
  
def get_page_text(formated_link: str, session: requests.Session) -> str:
  """accsept formated for search linc, get request, 
    configured session object and return page string

  Args:
      formated_link (str): linc formated for search
      session (requests.Session): configured session object

  Returns:
      str: page text based on search for link
  """
  resp = session.get(formated_link)
  print(f'resp.status_code: {resp.status_code}')
  if resp.status_code < 200 or resp.status_code >= 300: 
    sys.exit(f'resp.status_code: {resp.status_code}')
  return resp.text

def search_max_page_number(page_el: lxml.html.HtmlElement, 
                           paginator_xpat: str,
                           pagenumber_xpat: str) -> int:
  """accsept page HtmlElement, xpat for paginator and xpat for pagenumber and
    return total page number in paginator

  Args:
      page_el (lxml.html.HtmlElement): page in HtmlElement format
      paginator_xpat (str): xpat for extract pagenator block
      pagenumber_xpat (str): xpat for page number str
  Returns:
      int: total count of pages
  """
  paginator_el: lxml.html.HtmlElement = page_el.xpath(paginator_xpat)
  print(f'len(paginator_el): {len(paginator_el)}')
  if len(paginator_el) == 0: 
    sys.exit(f'len(paginator_el): {len(paginator_el)}')
  
  pagenumbers = paginator_el[0].xpath(pagenumber_xpat)
  if len(pagenumbers) == 0: 
    sys.exit(f'{len(pagenumbers).__str__()}: {len(pagenumbers)}')
  
  print(f'len(pagenumbers): {len(pagenumbers)}')
  total_pages = max(map(lambda pag_num: int(pag_num), pagenumbers))
  return total_pages
  

def prepare_session() -> requests.Session:
  """prepare session obgekt

  Returns:
      requests.Session: session
  """
  sesion = requests.Session()
  sesion.headers = util.load_header_dict_from_json(util.UBUNTY_HEADERS_JSON_FILE)
# sesion.cookies = util.get_cookies_from_general_file()
  if (os.environ.get('USERDOMAIN', 'NOT_VZLJOT') == 'VZLJOT'):
    sesion.proxies = util.VZLJOT_PROXY
  return sesion

def clean_str_in_list(list_str: list) -> list:
  """clean string in list

  Args:
      list_str (list): list string
  """
  # 'sjdflsdkjflksdfj'.strip()
  def clean(str_item: str):
    str_item = ' '.join(str_item.split())
    str_item = str_item.replace(u'\xa0', u' ')
    return str_item
  return list(map(clean, list_str))
  

  
def scrap_page(page_el: lxml.html.HtmlElement, targets_xpath_dict: dict) -> list:
  
  """accept page in HtmlElement format and dict xpath targets, 
  return list of tuple with value 

  Args:
      page_el (lxml.html.HtmlElement): page for search
      targets_xpath_dict (dict): dect of xpath
  Returns:
      list: [(val1.1, val1.2, ...), (val2.1, ...), (), ...]
  """
  result = []
  target_block_el: lxml.html.HtmlElement = page_el.xpath(targets_xpath_dict['target_block_xpath'])[0]
  target_elements_xpaths_dict: dict = targets_xpath_dict['target_elements_xpaths']
  for seatch_target, xpat in target_elements_xpaths_dict.items():
    seatch_target_value_list: list = target_block_el.xpath(xpat)
    cleaned_seatch_target_value_list = clean_str_in_list(seatch_target_value_list)
    result.append(cleaned_seatch_target_value_list)
  result = list(zip(*result))
  return result
  
def main(search_link: str, search_str: str, xpath_dict: dict):
  search_str_quoted = urllib.parse.quote_plus(search_str)
  search_link_quted = search_link
  next_page = 1
  total_pages = 1
  session = prepare_session()
  result = []
  
  with util.session_cookies_manage(session) as s:
    while next_page <= total_pages:
      current_linc = search_link_quted.format(searchString=search_str_quoted, pageNumber=next_page)
      if next_page == 1:
        # prepare_scrapping()

        page_text: str = get_page_text(current_linc, s)
        
        page_el: lxml.html.HtmlElement = lxml.html.fromstring(page_text)
        
        page_el.make_links_absolute(current_linc, resolve_base_href=True)
        
        total_pages = search_max_page_number(page_el, xpath_dict['paginator_xpath'], xpath_dict['pagenumber_xpath'])
        print(f'total_pages {total_pages}')

        # for testing purpose
        total_pages = 5 if total_pages > 5 else total_pages
        
        scrap_res = scrap_page(page_el, xpath_dict['scrap_targets'])
        
        result += scrap_res
        next_page += 1
        
      else:
        page_text: str = get_page_text(current_linc, s)
        
        page_el: lxml.html.HtmlElement = lxml.html.fromstring(page_text)
        
        page_el.make_links_absolute(current_linc, resolve_base_href=True)
        
        scrap_res = scrap_page(page_el, xpath_dict['scrap_targets'])
        
        result += scrap_res
        
        next_page += 1
  return result
 
      
def convert_list_tuple_rez_to_list_dict(schema: dict, list_rez: list) -> list:
  """accsept scheam in dict view and scrapping rez in list/tuple view
  and convert on in list/dict

  Args:
      schema (dict): _target_elements_xpaths dict_
      list_rez (list): [(val1.1, val1.2, ...), (val2.1, ...), (), ...]
  Returns:
  list: [{},{},{}]
  """
  keys = schema.keys()
  result = []
  for item in list_rez:
    target_dict= dict(zip(keys,item))
    result.append(target_dict)
  return result
  
          
        
        
# print(__name__)  
if __name__ == '__main__':
  
  search_link = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={searchString}&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={pageNumber}&sortDirection=false&recordsPerPage=_50&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1'
  
  search_str = 'топливо'
  
  xpath_dict = {
    'paginator_xpath': '//div[contains(@class, "paginator")]',
    'pagenumber_xpath': '//a[@data-pagenumber]/@data-pagenumber',
    'scrap_targets': {
      'target_block_xpath': "//div[@class='search-registry-entrys-block']",
      'target_elements_xpaths': {
        'тип_закупки': '//div[contains(@class,"registry-entry__header-top__title")]/text()[normalize-space()]',
        'рег_номер': '//div[contains(@class,"registry-entry__header-mid__number")]/a[1]/text()',
        'href_закупки': '//div[contains(@class,"registry-entry__header-mid__number")]/a[1]/@href',
        'этап_закупки': '//div[contains(@class,"registry-entry__header-mid__title")]/text()',
        'объект_закупки': '//div[div[normalize-space(.) = "Объект закупки"]]/div[position()=2]/text()',
        'заказчик': '//div[div[normalize-space(.) = "Заказчик"]]/div[position()=2]/a/text()',
        'href_заказчик': '//div[div[normalize-space(.) = "Заказчик"]]/div[position()=2]/a/@href',
        'начальная_цена': '//div[contains(@class, "price-block__value")]/text()',
        'размещено': '//div[div[normalize-space(.)="Размещено"]]/div[position()=2]/text()',
        'окончание_подачи': '//div[div[normalize-space(.)="Окончание подачи заявок"]]/div[position()=3]/text()'
      },  
    },
  }
  
  res = main(search_link=search_link, search_str=search_str, xpath_dict=xpath_dict)  
  schema = xpath_dict['scrap_targets']['target_elements_xpaths']
  dict_rez = convert_list_tuple_rez_to_list_dict(schema, res)

  pablic_res = {
    'data': strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),
    'search_link': search_link,
    'search_str': search_str,
    'result': dict_rez
  }
  
  with open('scrap-res.json', 'wt', encoding='utf-8') as f:
      json.dump(pablic_res, f, indent=4, ensure_ascii=False)