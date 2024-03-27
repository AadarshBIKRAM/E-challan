from flask import Flask, request, render_template, redirect, url_for
# from db_operations import adding, retriving
import pymysql


app = Flask(__name__)

conn = pymysql.connections.Connection(host='localhost', user='root', passwd='', database='e-challan')
cursor = conn.cursor()

@app.route('/')
# def welcome():
#     all_text = retriving()
#     return render_template('index.html', text=all_text)

def search():
    return render_template("checkRegistration.html")

@app.route('/checkRegistration', methods=['POST'])
def searchRegistration():
    registrationNumber = request.form['registrationNumber']

    cursor.execute("SELECT * FROM vehicleregistration WHERE registrationNumber = %s", (registrationNumber,))
    result = cursor.fetchone()

    return render_template('checkRegistration.html', registrationNumber=registrationNumber, result=result)

@app.route('/add-record', methods=['POST'])
def add_record():
    # Redirect to the page where record can be added
    return redirect(url_for('add_record_page'))

@app.route('/add-record-page')
def add_record_page():
    # Render the template for adding a record
    return render_template('newChallan.html')

# @app.route('/add_data', methods=['POST', 'GET'])
# def add_in_data():
#     if request.method == 'POST':
#         text_value = request.form['text1']
#         add_new = adding(text_value)
#         # return redirect(url_for('welcome'))
#         return render_template('trafficDb.html', textUsr=text_value)
#     else:
#         return redirect(url_for('welcome'))
        # return render_template('index.html', text='Failed')

# @app.route('/add_data/mainTask', methods=['POST'])
# def newChallan():
#         return render_template('newChallan.html')
#

if __name__ == '__main__':
    app.run(debug=True)

'''
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flsktest'
db = SQLAlchemy(app)
# Define a model for Person
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15))
# Create the tables
# db.create_all()
# Routes
@app.route('/')
def index():
    persons = Person.query.all()
    return render_template('index.html', persons=persons)
@app.route('/add', methods=['POST'])
def add_person():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    new_person = Person(name=name, email=email, phone=phone)
    db.session.add(new_person)
    db.session.commit()
    return redirect('/')
@app.route('/delete/<int:person_id>', methods=['POST'])
def delete_person(person_id):
    person = Person.query.get_or_404(person_id)
    db.session.delete(person)
    db.session.commit()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
    '''
