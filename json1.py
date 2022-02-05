import urllib.request, urllib.parse, urllib.error
import json

url = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('enter address: ')
    if len( address ) < 1:
        break

    url = url + urllib.parse.urlencode({'address': address})

    print('retrieving', url)
    uhand = urllib.request.urlopen(url)
    data = uhand.read().decode()
    print('retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' in js or js['status'] != 'OK':
        print('failed to retrieve data')
        print(data)
        continue

    print( json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted-address']
    print(location)
