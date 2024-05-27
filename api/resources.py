from flask_restful import Resource, reqparse
from models import Student, db

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('gender', type=str)
parser.add_argument('university', type=str)
parser.add_argument('email', type=str)
parser.add_argument('year_of_birth', type=int)

class StudentResource(Resource):
    def get(self, id):
        student = Student.query.get_or_404(id)
        return {'id': student.id, 'name': student.name, 'gender': student.gender, 'university': student.university, 'email': student.email, 'year_of_birth': student.year_of_birth}

    def put(self, id):
        args = parser.parse_args()
        student = Student.query.get_or_404(id)
        student.name = args['name']
        student.gender = args['gender']
        student.university = args['university']
        student.email= args['email']
        student.year_of_birth = args['year_of_birth']
        db.session.commit()
        return {'message': 'Student updated'}

    def delete(self, id):
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return {'message': 'Student deleted'}

class StudentListResource(Resource):

    def get(self):
        students = Student.query.all()
        return [{'id': student.id, 'name': student.name, 'gender': student.gender, 'university': student.university, 'email': student.email, 'year_of_birth': student.year_of_birth} for student in students]

    def post(self):
        args = parser.parse_args()
        print(args)
        id = 1
        students = Student.query.all()
        for student in students:
            if(id >= int(student.id)):
                id = int(student.id) + 1
        student = Student(name=args['name'], gender=args['gender'], university=args['university'], email=args['email'], year_of_birth = args['year_of_birth'])
        db.session.add(student)
        db.session.commit()
        return {'message': 'Student added'}, 201

                