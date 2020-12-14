import os
from config import db
from models import Person
# Data to initialize database with
People = [
    {'fname': 'Doug', 'lname': 'Farrell'},
    {'fname': 'Kent', 'lname': 'Brockman'},
    {'fname': 'Dazdraperma', 'lname': 'Mazolina'},
    {'fname': 'Maksim', 'lname': 'Makienko'},
    {'fname': 'Filya','lname': 'Gioveze'}
]
# Delete database file if it exists currently
if os.path.exists("people.db"):
    os.remove("people.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for person in People:
    p = Person(lname=person.get("lname"), fname=person.get("fname"))
    db.session.add(p)

db.session.commit()