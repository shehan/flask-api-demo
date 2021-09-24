import datetime
import json

from flask import jsonify, request
from flask_restful import Resource, abort

students = [
    {'id': 1, 'first_name': 'Tom', 'last_name': 'Green', 'DoB': datetime.datetime(1995, 5, 17)},
    {'id': 2, 'first_name': 'Peter', 'last_name': 'White', 'DoB': datetime.datetime(1996, 5, 10)},
    {'id': 3, 'first_name': 'Alice', 'last_name': 'Black', 'DoB': datetime.datetime(1995, 1, 1)},
    {'id': 4, 'first_name': 'Sarah', 'last_name': 'Silver', 'DoB': datetime.datetime(1997, 12, 1)},
    {'id': 5, 'first_name': 'Bob', 'last_name': 'Blue', 'DoB': datetime.datetime(1995, 2, 22)}
]


class Student(Resource):
    def get(self, student_id=None):
        record = [item for item in students if item.get('id') == student_id]
        if len(record) == 0:
            abort(404, message="Student {} doesn't exist".format(student_id))
        else:
            return jsonify(record)


class StudentList(Resource):
    def get(self):
        return jsonify(students)

    def post(self):
        if len(request.data) == 0:
            abort(400, message="No Student data provided in request")
        else:
            records = json.loads(request.data)
            inserted_id=[]
            for record in records:
                first_name = record['first_name']
                last_name = record['last_name']
                DoB = datetime.datetime.strptime(record['DoB'], '%Y-%m-%d').date()
                new_id = (max(students, key=lambda x: x['id'])['id']) + 1
                new_record = {'id': new_id, 'first_name': first_name, 'last_name': last_name, 'DoB': DoB}
                students.append(new_record)
                inserted_id.append(new_id)

            new_records = [element for element in students if element['id'] in inserted_id]
            return jsonify(new_records)
