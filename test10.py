from lxml import html
from lxml.html import HtmlElement
from urllib.request import urlopen

# root = html.parse(urlopen('http://httpbin.org/forms/post')).getroot()
root = html.parse('http://httpbin.org/forms/post').getroot()

# tree = html.parse(urlopen('http://httpbin.org/forms/post'))

print(type(root))
# print(type(tree))
html_str = html.tostring(root, pretty_print=True).decode()
# print(html_str)
root_dir = dir(root)
for men in root_dir:
    print(men)

