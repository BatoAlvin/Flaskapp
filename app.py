from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#Build an instance and store it in app
app = Flask(__name__)

#Define uri for db
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost/students'

#Create object
db=SQLAlchemy(app)

#Creating class for students
class Student(db.Model):
  __tablename__='students'
  id=db.Column(db.Integer,primary_key=True)
  fname=db.Column(db.String(40))
  location=db.Column(db.String(40))
  hobby=db.Column(db.String(40))

  def __init__(self,fname,location,hobby):
    self.fname=fname
    self.location=location
    self.hobby=hobby

#Build a get route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
   if request.method == 'POST': 
    fname= request.form['fname']
    location=request.form['location']
    hobby=request.form['hobby']

    student=Student(fname,location,hobby)
    db.session.add(student)
    db.session.commit()

    studentResult=db.session.query(Student).filter(Student.id==1)
    for result in studentResult:
     print(result.fname)

    return render_template('view.html', data={fname,hobby,location})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
   


if __name__ == "__main__":
    app.run(debug=True)    