import lxml
from lxml import etree
from io import BytesIO
from lxml.etree import ElementTree


tree: ElementTree = etree.parse('food.xml')
# with open('food.xml', 'rb') as f:
#     xml = f.read()

# tree = etree.XML(xml)
print(tree)
print(type(tree))

# etree_str = etree.tostring(tree, pretty_print=True)
# print(etree_str.decode())

# for el in tree.iter():
#     print(f'{el.tag} - {el.text}')

for el in tree.iter('price', 'name'):
    print(f'{el.tag} - {el.text}')
