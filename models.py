from datetime import datetime
from config import db, ma
from marshmallow_sqlalchemy import fields

class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key = True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow
    )

# To declare how Marshmallow should deserialize the Notes
class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_fk =True # include foreign key

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    fname = db.Column(db.String(32))
    # UTC = Coardinated Universal Time 
    timestamp = db.Column(
        db.DateTime, default= datetime.utcnow, onupdate= datetime.utcnow
    )
    notes = db.relationship(
        Note,
        backref = "person",
        cascade = "all, delete, delete-orphan",
        single_parent = True,
        order_by="desc(Note.timestamp)"
    )
# using Marshmallow(.ma) to inherit class from SQLAlchemyAutoSchema
# SQLAlchemy has data models
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True    # To deserialize JSON data and load Person Model instance
        sqla_session = db.session
        include_relationships = True #To include Note in Person
    notes = fields.Nested(NoteSchema, many= True)

# create instances
note_schema = NoteSchema()
person_schema = PersonSchema()
people_schema = PersonSchema(many = True)

