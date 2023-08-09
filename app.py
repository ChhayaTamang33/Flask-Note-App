from flask import render_template # Remove: import Flask
#import connexion
import sqlite3
import config
from models import Person

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

# conn = sqlite3.connect("people.db")
# cur = conn.cursor()
# cur.execute("SELECT * FROM person")

# people= cur.fetchall()
# for person in people:
#     print(person)

# columns = [
#     "id INTEGER PRIMARY KEY",
#     "lname VARCHAR UNIQUE",
#     "fname VARCHAR",
#     "timestamp DATETIME",
# ]
# create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
# conn.execute(create_table_cmd)

# people = [
#     "'1', 'Fairy', 'Tooth', '2022-08-05 09:15:10'",
#     "'2', 'Jolie', 'Angel', '2022-08-06 09:15:25'",
#     "'3', 'Smith', 'John', '2022-08-07 09:15:20'",
#     "'4', 'Tamang', 'Chhaya', '2022-08-08 09:15:15'"
# ]
# for person_data in people:
#     insert_cmd = f"INSERT INTO person VALUES ({person_data})"
#     conn.execute(insert_cmd)
# conn.commit()


# app = connexion.App(__name__, specification_dir="./")
# app.add_api("swagger.yml")

@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)