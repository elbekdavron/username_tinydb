from tinydb import TinyDB, Query
import requests

db = TinyDB('bd.json') 

headers = {
    'X-Api-Key':"4a322f608fd24b69ae2e0c50ecbfb2a3"
}

response = requests.get('https://randommer.io/api/Name?nameType=fullname&quantity=10', headers=headers).json()


for user in response:
    db.insert({'name':f"{user}"})

db.remove(doc_ids=range(1, 23))