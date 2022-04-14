from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), unique=True, nullable=False)
    personal_number = db.Column(db.Integer, unique=True, nullable=False)
    birthdate = db.Column(db.String(89), nullable=False)
    birthplace = db.Column(db.String(80), unique=True, nullable=False)
    department = db.relationship('Department', backref='person')
  
    def __repr__(self):
        return '<users %r>' % self.username
      
class Department(db.Model):
    department = db.Column(db.String(80), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),primary_key=True)

@app.route('/user/<int:id>')
def user(id):
    user=Person.query.filter_by(id=id)
    return render_template('user.html', user=user)

app.run(port=5000)
