from app import app, db
import models
from flask import request, abort, make_response
import json

@app.route('/')
def index():
    return "Employees management application"

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = models.Employee.query.all()
    employees = [e.dict() for e in employees]
    return json.dumps({'employees':employees})

@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = models.Employee.query.get(employee_id)
    if employee is None:
        abort(404)
    return json.dumps({'employee': employee.dict()})

@app.route('/employees/email/<employee_email>', methods=['GET'])
def get_employee_by_mail(employee_email):
    employees = models.Employee.query.filter(models.Employee.email.like("%" + employee_email + "%")).all()
    employees = [e.dict() for e in employees]
    return json.dumps({'employees': employees})

@app.route('/employees', methods=['POST'])
def create_employee():
    if not request.json or not 'first_name' in request.json or not 'second_name' in request.json or not 'email' in request.json:
        print "abort 400"
        abort(400)
    try:
        employee = models.Employee(first_name = request.json['first_name'], second_name = request.json['second_name'], email=request.json['email'])
        db.session.add(employee)
        db.session.commit()
    except Exception as e:
        abort(409)
    return json.dumps({'added': employee.dict()}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(json.dumps({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(json.dumps( { 'error': 'Bad request' } ), 400)

@app.errorhandler(409)
def not_found(error):
    return make_response(json.dumps( { 'error': 'Email already exists' } ), 409)


@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = models.Employee.query.get(employee_id)
    if employee is None:
        abort(404)
    db.session.delete(employee)
    db.session.commit()
    return json.dumps({'result': True})