import urllib.request
from urllib.request import urlopen
import json

from bs4 import BeautifulSoup

import urllib.request
import xmltodict

from xml.etree import ElementTree

#long/lat for Trondheim
req = urllib.request.urlopen('http://api.met.no/weatherapi/locationforecast/1.9/?lat=63.446827;lon=10.421906;msl=70') #http://www.nationaljournal.com/politics?rss=1


# for time in xml.findAll('time'):
#     print(time)

# xml = BeautifulSoup(read, 'xml')
read = req.read()#.decode()

# data = xmltodict.parse(read)



# print(data['weatherdata']['product'])
# print(data['weatherdata']['product']['time'][2]['@datatype'])
# print(data['weatherdata']['product']['time'][2])
# print(data['weatherdata']['product']['time'][32]['location']['symbol']['@id'])
# print(data['weatherdata']['product']['time'][32])
#
# for i in range(0,31):
#     try:
#         if(data['weatherdata']['product']['time'][i]['location']['symbol']['@id']) == 'Sun':
#             print(data['weatherdata']['product']['time'][i]['@from'])
#     except:
#         continue

data = ElementTree.parse(req)
print(data)
























