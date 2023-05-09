import urllib3
import json
url = "https://api.exchangerate.host/latest/"
http = urllib3.PoolManager()
response = http.request('GET', url)
data = response.data
currency = json.loads(data)
currency_data = currency['rates']
user = input('Enter the currency :')
for i, j in currency_data.items():
    if i == user:
        print("current vslue = ", j)