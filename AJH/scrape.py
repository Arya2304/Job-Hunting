import requests
proxy= '51.89.14.70'
try:
    r= requests.get('https://www.google.com/',proxies={'http':proxy,'http':proxy},timeout=3)
    print(r.json())
except:
    print('failed')
    pass