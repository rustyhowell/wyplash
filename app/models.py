from app import db

class TestSuite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<TestSuite {}>'.format(self.name)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    classname = db.Column(db.String(64), index=True, unique=True)
    line = db.Column(db.Integer)
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<Test {}>'.format(self.name)


class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<TestResult {}>'.format(self.name)
