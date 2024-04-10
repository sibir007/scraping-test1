import urllib
from urllib import request
from urllib import response
from http.client import HTTPResponse
import urllib.error as err
import urllib.parse as prs


link='https://www.google.com'
amazonUrl ='https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books'
pLink = prs.urlparse(amazonUrl)
data = {
    'param1': ['value1', 'value2'],
    'patam2': 'value3'
}
data_str = prs.urlencode(data)
data_str_unquot = prs.unquote_plus(data_str)
data_back = prs.parse_qs(data_str_unquot)


print(data_str)
print(data_str_unquot)
print(data_back)
# for k in pLink.keys:
#     print(k, pLink[k])
print(prs.unquote_plus(pLink.query))
try:
    linkRequest: HTTPResponse = request.urlopen(link)
    # print(linkRequest)
    print(type(linkRequest))
    print(linkRequest.getcode())
    print(linkRequest.geturl())

    # print(linkRequest.getheaders().__str__())

    linkResponse = linkRequest.read()
    print(type(linkResponse))
except err.URLError as e:
    print('Error :', e.reason)
except err.HTTPError as e:
    print('Error: ', e.reason)

requestObj = request.Request('https://www.samsclub.com/robots.txt')
print(type(requestObj))
requestObjResponse: HTTPResponse = request.urlopen(requestObj)
print(type(requestObjResponse))
print(requestObjResponse.geturl())