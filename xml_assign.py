import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
'''
api_key = False
print('apikey ',api_key)
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
    print('service ',serviceurl)
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
'''
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#address = input('Enter url: ')
address = 'http://py4e-data.dr-chuck.net/comments_199797.xml'
if len(address) < 1: exit()
'''
parms = dict()
parms['address'] = address
if api_key is not False:
    parms['key'] = api_key
'''
#url = serviceurl + urllib.parse.urlencode(parms)
url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
#print('uh',uh)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
#print('tree = ',tree)

counts = tree.findall('.//count')
sum = 0
print('count:',len(counts))
for i in range (0,len(counts)):
    num = int(counts[i].text)
    sum +=num
print('sum = ',sum)
