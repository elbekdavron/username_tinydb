from tinydb import TinyDB


db = TinyDB('books_db.json')

books = [
    {"name": "The Psychology of Money", "author": "Morgan Housel", "year": 2020, "genre": "Self-help", "publisher": "Harriman House"},
    {"name": "Outliers", "author": "Malcolm Gladwell", "year": 2011, "genre": "Self-help", "publisher": "Back Bay Books"},
    {"name": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian", "publisher": "Secker & Warburg"},
    {"name": "Animal Farm", "author": "George Orwell", "year": 1945, "genre": "Dystopian", "publisher": "Secker and Warburg"},
    {"name": "Days Gone by", "author": "Abdulla Qodiriy", "year": 1922, "genre": "Historical Fiction", "publisher": "LP"},
    {"name": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "genre": "Fantasy", "publisher": "George Allen & Unwin"},
    {"name": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953, "genre": "Dystopian", "publisher": "Ballantine Books"},
    {"name": "The Anomaly", "author": "Hervé Le Tellier", "year": 2020, "genre": "Science fiction", "publisher": "Éditions Gallimard"},
    {"name": "War and Peace", "author": "Leo Tolstoy", "year": 1869, "genre": "Historical Fiction", "publisher": "The Russian Messenger"},
    {"name": "Educated", "author": "Tara Westover", "year": 2018, "genre": "Biography", "publisher": "Random House"},
    {"name": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866, "genre": "Psychological Fiction", "publisher": "The Russian Messenger"},
    {"name": "Message to a citizen", "author": "Yulo Vooglaid", "year": 1975, "genre": "Dystopian", "publisher": "Samizdat"},
    {"name": "Steve Jobs", "author": "Walter Isaacson", "year": 2011, "genre": "Biography", "publisher": "Simon & Schuster"},
    {"name": "Bank 4.0", "author": "Brett King", "year": 2018, "genre": "Finance", "publisher": "Marshall Cavendish International"},
    {"name": "Why Nations Fail", "author": "Daron Acemoglu and James A. Robinson", "year": 2012, "genre": "Economics", "publisher": "Random House"},
    {"name": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954, "genre": "Fantasy", "publisher": "George Allen & Unwin"},
    {"name": "The Alchemist", "author": "Paulo Coelho", "year": 1988, "genre": "Fantasy", "publisher": "HarperTorch"},
    {"name": "The Little Prince", "author": "Antoine de Saint-Exupéry", "year": 1943, "genre": "Fantasy", "publisher": "Reynal & Hitchcock"},
    {"name": "Deep Work", "author": "Cal Newport", "year": 2016, "genre": "Self-help", "publisher": "Grand Central Publishing"},
    {"name": "Zero to One", "author": "Peter Thiel", "year": 2014, "genre": "Business", "publisher": "Crown Business"}
]


db.insert_multiple(books)