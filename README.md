# RESTapi-project - employees management project

This is a server application, which offers a simple REST API to employees management in a small company. The application uses Flask framework. Data are stored in SQLite database.  

## Project deployment on Linux ##

### Requirements: ###
- python
- python-pip
- curl

### Installing: ###
```
git clone https://github.com/magdamagda/RESTapi-project.git <your directory>
pip install -r requirements.txt

cd <your directory>
python db_create.py
python db_migrate.py
python db_upgrade.py
```
### Run aplication: ###
```
python run.py
```
### Application unit tests: ###
```
python tests.py
```
### API description: ###
 - display employees
 ```
     Method: GET
     /employees
 ```
 - add employee
 ```
 Method: POST
 Data: {"first_name":"<first name>", "last_name":"<last name>", "email":"<email>"}
 Content-Type: application/json
 /employees
 ```
 - display employee by id
 ```
 Method: GET
 /employees/<id>
 ```
 - filter employees by mail
 ```
 Method: GET
 /email/<email>
 ```
 - delete employee by id
 ```
 Method: DELETE
 /employees/<id>
 ```

### Example how to use the application (with curl on Linux): ###
 - display employees
 ```
 curl -i http://localhost:5000/employees
 ```
 - add employee
 ```
 curl -i -H "Content-Type: application/json" -X POST -d '{"first_name":"<first name>", "last_name":"<last name>", "email":"<email>"}' http://localhost:5000/employees
 ```
 - display employee by id
 ```
 curl -i http://localhost:5000/employees/<id>
 ```
 - filter employees by mail
 ```
 curl -i http://localhost:5000/email/<email>
 ```
 - delete employee
 ```
 curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/employees/<id>
 ```



