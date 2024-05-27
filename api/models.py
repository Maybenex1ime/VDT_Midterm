from database import db

class Student(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    university = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable = False)
    year_of_birth = db.Column(db.Integer(), nullable = False)