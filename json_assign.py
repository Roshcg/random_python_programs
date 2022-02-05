import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_199798.json'
if len( url ) < 1:
    exit()

print('retrieving', url)
uhand = urllib.request.urlopen(url)
data = uhand.read().decode()
print('retrieved', len(data), 'characters')

info = json.loads(data)
print(info)
print('User count:', len(info['comments']))
sum = 0
for i in range ( 0, len(info['comments'])):
    sum = sum + int(info['comments'][i]['count'])
print(sum)