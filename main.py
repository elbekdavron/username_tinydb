from tinydb import TinyDB

db = TinyDB('db.json') 

db.insert(
    {
        'name': 'Behzod', 
        'age': 35, 
        'job': 'economist'
    }
)
db.insert(
    {
        'name': 'Akobir', 
        'age': 19, 
        'job': 'teacher'
    }
)

