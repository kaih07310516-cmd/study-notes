import urllib.request,urllib.parse
import http,json,ssl

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'
# 忽略 SSL 证书错误（初始化 ctx）
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location:')
    if len(address)<1:
        break
    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving',url)
    uh = urllib.request.urlopen(url,context=ctx)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters',data[ :20].replace('\n',' '))

    js = json.loads(data)

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat',lat,'lon',lon)
    location = js['features'][0]['properties']['formatted']
    print(location)