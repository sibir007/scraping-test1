from lxml import html
from lxml.html import HtmlElement, FormElement
import requests
from requests import Response


resp: Response = requests.get('http://httpbin.org/forms/post')
tree: HtmlElement = html.fromstring(resp.text)
for el in tree.iter('input'):
    print(
        f'Element: {el.tag}',
        f'\n\tvalues(): {el.values()}',
        f'\n\tattribu: {el.attrib}'
        f'\n\titems(): {el.items()}',
        f'\n\tkeys() {el.keys()}', 
        end='\n'
          )
