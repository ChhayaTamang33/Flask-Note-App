from datetime import datetime
from config import app, db
from models import Person, Note

PEOPLE_NOTES = [
    {
        "lname": "Tamang",
        "fname": "Chhaya",
        "notes": [
            ("I always make my bed after I wake up.", "2022-01-06 17:10:24"),
            ("I have to buy white sneakers.", "2022-03-05 22:17:54"),
            ("I always play games.", "2022-03-05 22:18:10"),
        ],
    },
    {
        "lname": "Jolie",
        "fname": "Angelina",
        "notes": [
            ("She is a great Actor.", "2022-01-01 09:15:03"),
            ("Really! She played Maleficent?", "2022-02-06 13:09:21"),
        ],
    },
    {
        "lname": "Rain",
        "fname": "Amber",
        "notes": [
            ("She is a very good singer.", "2022-01-07 22:47:54"),
            ("It's her time to shine.", "2022-04-06 13:03:17"),
        ],
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in PEOPLE_NOTES:
        new_person = Person(lname=data.get("lname"), fname=data.get("fname"))
        for content, timestamp in data.get("notes", []):
            new_person.notes.append(
                Note(
                    content=content,
                    timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                )
            )
        db.session.add(new_person)
    db.session.commit()