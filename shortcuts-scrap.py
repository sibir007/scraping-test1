import lxml
# import lxml.etree
# import lxml.html
import lxml.html
import requests
import util
# res = requests.get('https://www.maketecheasier.com/cheatsheet/vscode-keyboard-shortcuts/')

# root: lxml.html.HtmlElement = lxml.html.parse('https://www.maketecheasier.com/cheatsheet/vscode-keyboard-shortcuts/').root()

# tr_els = root.xpath

root: lxml.html.HtmlElement = lxml.html.parse('shortcuts.html')


# razd = '//*[@style="text-decoration:underline"]' #remove 1
# action = '//*[@class="row-hover"]//*[@class="column-1"]'
# win = '//*[@class="row-hover"]//*[@class="column-2"]'
# lin = '//*[@class="row-hover"]//*[@class="column-4"]'
# tr_els = root.xpath(razd)
# tbody = root.xpath('//tbody')[0]
trs_xpath = '//tbody/tr'

trs_list = root.xpath('//tbody//tr')

res = {}
current_key = ''
print(len(trs_list))
for tr in trs_list:
    # print(td.text)
    for td in tr:
        if td.text == None:
            # print(td.text)
            current_key = tr.xpath('string()')
            print(current_key)
            break
            # td[0]
            