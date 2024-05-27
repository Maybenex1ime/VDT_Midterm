import unittest
import requests

BASE_URL = 'http://127.0.0.1:5000/api/students'

class TestAPI(unittest.TestCase):

    def test_get_students(self):
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)

    def test_create_student(self):
        new_student = {'name': 'Thinh', 'gender': 'Nam', 'university': 'ITMO university', 'year_of_birth': 2001, 'email': 'thinh@gmail.com'}
        response = requests.post(BASE_URL, json=new_student)
        self.assertEqual(response.status_code, 201)

    def test_update_student(self):
        student_id = 1
        updated_student = {'name': 'Manh', 'gender': 'Nam', 'university': 'ITMO university', 'year_of_birth': 2001, 'email': 'manh@gmail.com'}
        response = requests.put(f"{BASE_URL}/{student_id}", json=updated_student)
        self.assertEqual(response.status_code, 200)

    def test_delete_student(self):
        student_id = 2
        response = requests.delete(f"{BASE_URL}/{student_id}")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
