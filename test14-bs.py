import bs4
import util

def bs_version():
    print(bs4.__version__)

def bs_dir():
    for item in dir(bs4):
        if item.startswith('__') or item.startswith('_'): continue
        print(item)
        
# bs_version()
# bs_dir()

with open('shortcuts.html', 'rb') as f:
    b_html_marku = f.read()
soup = bs4.BeautifulSoup(b_html_marku, 'lxml')
print(type(soup))
# soup_pret = soup.prettify()

# with open('shortcuts.pr.html', 'wt', encoding='utf-8') as f:
#     f.write(soup_pret)

print(soup.li.has_attr('td'))
# print(soup.find('tbody'))
print(soup.findAll('tr'))
print(soup.find(string='Python'))

