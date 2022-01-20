from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class db_student(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   email = db.Column(db.String(50))
   #menggunakan Date error
   date = db.Column(db.String(50)) 
   age = db.Column(db.Integer)

def __init__(self, name, email, date,age):
   self.name = name
   self.email = email
   self.date = date
   self.age = age

@app.route('/')
def show_all():
   return render_template('show_all.html', db_student = db_student.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['email'] or not request.form['date']:
         flash('Please enter all the fields', 'error')
      else:
         student = db_student(name=request.form['name'], email=request.form['email'], date=request.form['date'], age=request.form['age'])
         
         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
