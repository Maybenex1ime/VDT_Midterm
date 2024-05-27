import os
import csv
from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
from resources import StudentResource, StudentListResource
from database import db
from models import Student

app = Flask(__name__)
api = Api(app)
CORS(app,origins = ["http://localhost:3000"])

API_URL = 'http://localhost:5000/api/students'

api.add_resource(StudentListResource, '/api/students')
api.add_resource(StudentResource, '/api/students/<int:id>')

if __name__ == '__main__':
    app.config.from_pyfile("config.py")
    db.init_app(app)
    with app.app_context():
        db.create_all()
        with open("VDT_Cloud_2024.csv",encoding = "utf-8-sig",mode = "r") as f:
            db.session.query(Student).delete()
            reader = csv.reader(f)
            header = next(reader)
            for i in reader:
                kwargs = {column: value for column, value in zip(header, i)}
                new_entry = Student(**kwargs)
                db.session.add(new_entry)
                db.session.commit()
    app.run(debug=False, port=5000)
