# RESTapi-project - employees management project

## Project deployment ##

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
### Running aplication: ###
```
python run.py
```
### Testing application: ###
```
python tests.py
```
### Using application (using curl on Linux): ###
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



