#!flask/bin/python
from app import app
print "running"
app.run(debug=True, host='0.0.0.0')