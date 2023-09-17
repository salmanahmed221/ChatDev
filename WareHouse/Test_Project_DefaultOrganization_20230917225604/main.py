'''
This is the main file for the Flask app.
'''
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import StudentForm
from database import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)
from models import Student
@app.route('/', methods=['GET', 'POST'])
def index():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(
            name=form.name.data,
            age=form.age.data,
            education=form.education.data,
            address=form.address.data,
            city=form.city.data,
            phone_number=form.phone_number.data
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)
@app.route('/success')
def success():
    return render_template('success.html')
if __name__ == '__main__':
    app.run(debug=True)