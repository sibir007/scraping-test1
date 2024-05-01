from selenium import webdriver
from typing import List, Iterable, Mapping, Union
from selenium.webdriver import FirefoxOptions, FirefoxProfile, Firefox, FirefoxService
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from selenium.common.exceptions import NoSuchElementException
from time import gmtime, strftime
from urllib import parse
import csv
from pathlib import Path
import os
import re

class NotDefinedWebElement:
    """ Элемент заглушка. В случае когда WebElement.find_element() метод
    бросает исключение NoSuchElementException, функция или метод перехватывающее
    это исключение может вернуть экземпляр NotDefinedWebElement, любые дальнейшие
    способы использования данного объекта будут возвращать строку "Not defined" 
    """
    
    def __getattr__(self, name):
        return self
    
    def __repr__(self) -> str:
        return 'Not defined'

    def __call__(self, *args: expected_conditions.Any, **kwds: expected_conditions.Any) -> expected_conditions.Any:
        return 'Not defined'

link_zak_home = 'https://zakupki.gov.ru/epz/main/public/home.html'
link_zak_search = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html'

ELEMENTS_LIST_XPATH = '//div[contains(@class, "search-registry-entry-block")]'
NEXT_PAGE_XPATH = '//a[contains(@class, "paginator-button-next")]'
PROFILE_DIR = '.browsers/firefox/profile/'
CACHE_DIR = os.path.abspath('.browsers/firefox/cache/')

OPTIONS = {
    'geo.enabled': False,
    'geo.provider.use_corelocation': False,
    'geo.prompt.testing': False,
    'geo.prompt.testing.allow': False,
    'browser.cache.disk.parent_directory': CACHE_DIR,
}

RK = re.compile('\s+')

def main():
    # cache_dir = CACHE_DIR
    profile = FirefoxProfile()
    # profile.set_preference('browser.cache.disk.parent_directory', CACHE_DIR)
    profile._profile_dir = PROFILE_DIR
    # os.chmod(profile._profile_dir, 0o755)
    
    options = Options()
    options.profile = profile
    # 'normal' (default)	complete	Used by default, waits for all resources to download
    # 'eager'	interactive	DOM access is ready, but other resources like images may still be loading
    # 'none'	Any	Does not block WebDriver at all
    # options.page_load_strategy = 'normal'

    for k_option, v_option in OPTIONS.items():
        options.set_preference(k_option, v_option)

    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, timeout=5)

    driver.get(link_zak_home)
    # print_search_input(driver)
    

    zakup_link = driver.find_element(By.XPATH, '//a[contains(@class, "main-link  _order ")]')
    # wait.until(lambda d: zakup_link.is_displayed())
    zakup_link.click()
    # print_element(driver)
    search_input = driver.find_element(By.XPATH, '//*[@id="searchString"]')
    
    # print(f'search_input: {search_input}')
    # wait.until(lambda _: search_input.is_displayed())
    search_input.send_keys('Приборы учёта')

    search_button = driver.find_element(By.XPATH, '//button[contains(@class, "search__btn")]')
# //button[contains(@class, "search__btn")]
# //*[@id="searchString"]
    search_button.click()

# //*[@id="_50"]
    select_record_per_page_el = driver.find_element(By.XPATH, '//div[contains(@class, "select-record-per-page--number")]')
    select_record_per_page_el.click()
    select_num_items_50 = driver.find_element(By.XPATH, '//*[@id="_50"]')

    # wait.until(lambda _: select_num_items.is_displayed())
# select_num_items.
    select_num_items_50.click()
    # print_element(driver)


    # time.sleep(10)
    
    items_list: List[WebElement] = extract_elements_list(driver, ELEMENTS_LIST_XPATH)

    # fz = parse.urljoin(driver.current_url, items_list[0].find_element(By.XPATH, './/div[contains(@class, "registry-entry__header-mid__number")]/a').text)
    # fz = items_list[0].find_element(By.XPATH, '//div[contains(@class, "registry-entry__header-top__title")]').text
    # fz = items_list[0].find_element(By.XPATH, './/div[contains(@class, "registry-entry__header-mid__number")]/a').get_attribute('href')
    # print(type(fz))
    # print(fz)
    # print_element(driver)
    store_elemen_coru = store_elemen()
    prosess_element_list(items_list, driver, store_elemen_coru)
    count_pages = 4
    try:
        # while True:
        while count_pages := count_pages -1 :
            next_page_el: WebElement = driver.find_element(By.XPATH, NEXT_PAGE_XPATH)
            next_page_el.click()
            # print_element(driver)
            items_list: List[WebElement] = extract_elements_list(driver, ELEMENTS_LIST_XPATH)
            # items_list.extend()
            prosess_element_list(items_list, driver, store_elemen_coru)
    except NoSuchElementException as e:
        store_elemen_coru.throw(StopIteration())
        print('NoSuchElementException rised: pages are out')
        
    # print(len(items_list))
    # return driver
    # driver.get_cookies()
    # driver.add_cookie()
    driver.quit()
    
def print_element(driver: Firefox):
    """Для проверки идентичности элементов после click()

    Args:
        driver (Firefox): driver
    """     
    search_input = driver.find_element(By.XPATH, './/div[contains(@class, "registry-entry__header-mid__number")]/a').text
    # search_input = driver.find_element(By.XPATH, '//*[@id="searchString"]')
    print(f'search_input: {search_input}')

def extract_elements_list(driver: Firefox, xpath: str) -> List[WebElement]:
    return driver.find_elements(By.XPATH, xpath)


def prosess_element_list(elements_list: List[WebElement], driver: Firefox, store_elemen_coru) -> None:
    # store_elemen_coru = store_elemen()
    for item in get_items(elements_list, driver):
        c_item = clean_item(item)
        store_elemen_coru.send(c_item)
    



def get_items(elements_list: List[WebElement], driver: Firefox) -> Iterable[Mapping[str, str]]:
    for element in elements_list:
        item = {            
            'date': strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),
            'fz': 'not defined' if not (res := find_element_or_none(element, './/div[contains(@class, "registry-entry__header-top__title")]')) else res.text,
            'reg_num': 'not defined' if not (res := find_element_or_none(element, './/div[contains(@class, "registry-entry__header-mid__number")]/a')) else res.text,
            'reg_num_href': 'not defined' if not (res := find_element_or_none(element, './/div[contains(@class, "registry-entry__header-mid__number")]/a')) else res.get_attribute('href'),
            'stage': 'not defined' if not (res := find_element_or_none(element, './/div[contains(@class, "registry-entry__header-mid__title")]')) else res.text,
            'p_object': 'not defined' if not (res := find_element_or_none(element, './/div[contains(@class, "registry-entry__body-value")]')) else res.text,
            'organization_type': 'not defined' if not (res := find_element_or_none(element, './/div[@class="registry-entry__body"]/child::*[2]/child::*[1]')) else res.text,
            'organization_name': 'not defined' if not (res := find_element_or_none(element, './/div[contains(@class, "registry-entry__body-href")]/a')) else res.text,
            'organization_href': 'not defined' if not (res := find_element_or_none(element, './/div[contains(@class, "registry-entry__body-href")]/a')) else res.get_attribute('href'),
            's_price': 'not defined' if not (res := find_element_or_none(element, './/div[contains(@class, "price-block__value")]')) else res.text,
            'posted': 'not defined' if not (res := find_element_or_none(element, './/div[normalize-space(.)="Размещено"]/parent::*/div[2]')) else res.text,
            'updated': 'not defined' if not (res := find_element_or_none(element, './/div[normalize-space(.)="Обновлено"]/parent::*/div[2]')) else res.text,
            'ending': 'not defined' if not (res := find_element_or_none(element, './/div[normalize-space(.)="Окончание подачи заявок"]/following-sibling::div[1]')) else res.text,
            'documents_href': 'not defined' if not (res := find_element_or_none(element, './/a[normalize-space(.)="Документы"]')) else res.get_attribute('href'),
        }
        yield item

def find_element_or_none(element: WebElement, xpath: str) -> Union[WebElement, None]:
    """Если element.find_element() бросает исключение NoSuchElementException
    то функция возвращает None, в противном случае возвращает
    результат element.find_element()

    Args:
        element (WebElement): WebElement объект
        xpath (str): xpath

    Returns:
        Union[WebElement, None]: результат element.find_element() оr None
    """
    try:
        result: WebElement = element.find_element(By.XPATH, xpath)
    except NoSuchElementException as e:
        result: None = None
    return result
        

        
        
def clean_item(item: Mapping[str, str]) -> Mapping[str, str]:
    item = {k: RK.sub(' ', v).strip() for k, v in item.items()}
    return item

def store_elemen():
    def corutine_f():
        file = Path('zakupki2.csv')
        # if not file.exists():
        with open(file, 'w') as csv_file:
            item = yield
            fields_name = item.keys()
            writer = csv.DictWriter(csv_file, fieldnames=fields_name)
            writer.writeheader()
            writer.writerow(item)
            try:
                while True:
                    item = yield
                    writer.writerow(item)
            except StopIteration as e:
                pass
    coru = corutine_f()
    next(coru)
    return coru
                
    # else:
    #     with open(file, 'wa') as csv_file:
    #         fields_name = item.keys()
    #         writer = csv.DictWriter(csv_file, fieldnames=fields_name)
            
    #         writer.writerow(item)


if __name__ == '__main__':
    main()