from app import app, db, models
import unittest
from config import basedir
import os
import json

class AppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        db.create_all()
        employees = models.Employee.query.all()
        for e in employees:
            db.session.delete(e)
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test1_main_page(self):
        result = self.app.get('/')

        self.assertEqual(result.status_code, 200)

    def test2_empty_employees(self):
        result = self.app.get('/employees')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, json.dumps({"employees" : []}))

    def test3_employee_not_found(self):
        result = self.app.get('/employees/1')
        self.assertEqual(result.status_code, 404)

    def test4_empty_employees_by_mail(self):
        result = self.app.get('/employees/email/abcd@abcd')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, json.dumps({"employees": []}))

    def test5_delete_empty_employee(self):
        result = self.app.delete('/employees/1')
        self.assertEqual(result.status_code, 404)

    def test6_add_employee(self):
        result = self.app.post('/employees',
                                data="not a json",
                                content_type='application/json')
        self.assertEqual(result.status_code, 400)

        data = {'first_name':'Jan', 'second_name':'Kowalski', 'email':'jan@kowalski'}
        result = self.app.post('/employees',
                               data=json.dumps(data),
                               content_type='application/json')
        self.assertEqual(result.status_code, 201)
        response = json.loads(result.data)
        self.assertTrue("added" in response)
        self.assertEqual(data["first_name"], response["added"]["first_name"])
        self.assertEqual(data["second_name"], response["added"]["second_name"])
        self.assertEqual(data["email"], response["added"]["email"])

        data = {'first_name': 'Jan', 'second_name': 'Kowalski', 'email': 'jan@kowalski'}
        result = self.app.post('/employees',
                               data=json.dumps(data),
                               content_type='application/json')
        self.assertEqual(result.status_code, 409)

        data = {'first_name': 'Jan2', 'second_name': 'Kowalski2', 'email': 'jan@kowalski2'}
        result = self.app.post('/employees',
                               data=json.dumps(data),
                               content_type='application/json')
        self.assertEqual(result.status_code, 201)
        response = json.loads(result.data)
        self.assertTrue("added" in response)
        self.assertEqual(data["first_name"], response["added"]["first_name"])
        self.assertEqual(data["second_name"], response["added"]["second_name"])
        self.assertEqual(data["email"], response["added"]["email"])

    def test7_get_delete_employees(self):
        result = self.app.get('/employees')
        self.assertEqual(result.status_code, 200)
        response = json.loads(result.data)
        self.assertTrue("employees" in response)
        self.assertEqual(len(response['employees']), 2)

        employee = response['employees'][0]
        result = self.app.get('/employees/' + str(employee["id"]))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), {'employee': employee})

        result = self.app.get('/employees/email/' + employee["email"])
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data), {'employees': [employee]})

        result = self.app.delete('/employees/' + str(employee["id"]))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, json.dumps({'result': True}))
        employees = models.Employee.query.all()
        self.assertEqual(len(employees), 1)


if __name__ == '__main__':
    unittest.main()

