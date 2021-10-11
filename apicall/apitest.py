import requests


res = requests.get("http://127.0.0.1:8000/loadallpersons/")

res2 = requests.get("http://127.0.0.1:8000/loadpersonbyid/3")

t2 = res2.json()
t = res.json()

if t2 != None:
    for p in t2:
        print(p)

