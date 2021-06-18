import requests

print("hello gaes")

try:
    r = requests.get('https://goo gle.com')
    print(r.status_code)
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print('Ada error', e)