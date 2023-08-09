# from datetime import datetime
from flask import abort, make_response
from config import db
from models import Person, people_schema, person_schema

# def get_timestamp():
#     return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# PEOPLE = {
#     "Fairy": {
#         "fname": "Tooth",
#         "lname": "Fairy",
#         "timestamp": get_timestamp(),
#     },
#     "Ruprecht": {
#         "fname": "Knecht",
#         "lname": "Ruprecht",
#         "timestamp": get_timestamp(),
#     },
#     "Bunny": {
#         "fname": "Easter",
#         "lname": "Bunny",
#         "timestamp": get_timestamp(),
#     },
#     "Tamang": {
#         "fname": "Chhaya",
#         "lname": "Tamang",
#         "timestamp": get_timestamp(),
#     }
# }

def read_all():
    people = Person.query.all()
    #person_schema = PersonSchema(many=True)
    return people_schema.dump(people)
    # return list(PEOPLE.values())

def read_one(lname):
    person = Person.query.filter(Person.lname == lname).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )

def create(person):
    lname = person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session =db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    
    else:
        abort(
            406,
            f"Person with last name {lname} already exists",
        )

def update(lname, person):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()
    if existing_person:
        update_person = person_schema.load(person, session = db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )

def delete(lname):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{lname} successfullt deleted", 200)
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )