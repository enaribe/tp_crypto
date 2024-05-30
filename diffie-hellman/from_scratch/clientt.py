import requests
import random

p = 23
g = 5

#generer laa cle publique
xb = random.randint(2, p-1)
PubB = pow(g, xb, p)
data = {'public_key': PubB}
response = requests.post('http://127.0.0.1:5000/key_exchange', json=data)
print(response.text)
pubS = response.json()["public_key"]
print(pubS)
share = pow(pubS, xb, p)
print("share : ", share)