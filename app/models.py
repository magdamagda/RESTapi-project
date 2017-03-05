from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    second_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '%r %r %r' % (self.first_name, self.second_name, self.email)

    def dict(self):
        return {"id": self.id, "first_name": self.first_name, "second_name": self.second_name, "email" : self.email}