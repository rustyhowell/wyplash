from app import db

class TestSuite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<TestSuite {}>'.format(self.name)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    classname = db.Column(db.String(64), index=True)
    line = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    status = db.Column(db.Integer)
    failure_message = db.Column(db.String(256))
    stacktrace = db.Column(db.String(256))

    def __repr__(self):
        return '<Test {}>'.format(self.name)


class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<TestResult {}>'.format(self.name)
