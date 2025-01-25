from tinydb import TinyDB

db = TinyDB('db.json') 

db.insert({'name': 'Zarif', 'age': 35})
