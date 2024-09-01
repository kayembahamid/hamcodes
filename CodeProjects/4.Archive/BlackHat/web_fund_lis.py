# url = 'https://www.nostarch.com'
# response = urllib3.urlopen(url) # GET
# print(response.read())
# response.close()


# url = "https://www.nostarch.com"
# headers = {'User-Agent': "Googlebot"}
# request = urllib3.Request(url, headers=headers)
# response = urllib3.urlopen(request)
# print(response.read())
# response.close()

import urllib
import urllib3
import urllib.parse
import urllib.request
import requests
from io import BytesIO
from lxml import etree

# url = 'http://boodelyboo.com'
# with urllib.request.urlopen(url) as response:  # GET
#    content = response.read()
# print(content)

# info = {'user': 'tim', 'passwd': '31337'}
# data = urllib.parse.urlencoode(info).encode() # data is now of type bytes
# req = urllib.resquest.Request(url, data)
# with urllib.request.urlopen(req) as response: # POST
#   content = response.read()
# print(content)

# url = 'http:boodelyboo.com'
# response = requests.get(url) # GET
# data = {'user': 'tim', 'passwd': '31337'}
# response = requests.post(url, data=data)  # POST
# print(response.text)  # response.text = string; response.content = bytestring

url = 'https://nostarch.com'
r = requests.get(url)  # GET
content = r.content   # content is of type 'bytes'
parser = etree.HTMLParser()
content = etree.parse(BytesIO(content),parser=parser) # Parse into tree
for link in content.findall('//a'):  # find all "a" anchor elements.
    print(f"{link.get('href')} -> {link.text}")

from bs4 import BeautifulSoup as bs
url = 'http://bring.com'
r = requests.get(url)
tree = bs(r.text, 'html.parser') # Parse into tree
for link in tree.find_all('a'):  # find all "a" anchor elements.
    print(f"{link.get('href')} -> {link.text}")
    






