# import Flask
from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
# the "re" module will let us perform some regular expression operations
import re
import md5
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector(app,'regislog')
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
	email = request.form['email'];
	firstN = request.form['first'];
	lastN = request.form['last'];
	pwd = request.form['password'];
	pwdCon = request.form['password2'];

	errors = False;
	print errors

	if len(firstN) < 2:
		flash("First Name - letters only, at least 2 characters")
		errors = True;
	if len(lastN) < 2:
		flash("First Name - letters only, at least 2 characters")
		errors = True;
	if not firstN.isalpha() or not lastN.isalpha():
		flash("First and last name should not comtain number(s)")
		errors = True;
	if len(email) < 1:
		flash("Email cannot be blank!")
		errors = True;
	if not EMAIL_REGEX.match(email):
		flash("Invalid Email Address!")
		errors = True;
	if len(pwd) < 8:
		flash("Password should not be less than 8 characters")
		errors = True;
	if pwd != pwdCon:
		flash("Password and Confirm Password are not match")
		errors = True;
	if not errors:
		query = "INSERT INTO regislog (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
		data = {
	             'first_name': firstN, 
	             'last_name':  lastN,
	             'email': email,
	             'password': md5.new(pwd).hexdigest()
	           }
		mysql.query_db(query, data)
		flash("Your Registration is successful!!")
    	return redirect('/')
	return redirect('/')

@app.route('/login', methods=['POST'])
def login():
	query = "SELECT email, password FROM regislog WHERE email = :email and password = :password"
    # Then define a dictionary with key that matches :variable_name in query.
	data = {'email': request.form['email'],
			'password': md5.new(request.form['password']).hexdigest()}
    # Run query with inserted data.
	friends = mysql.query_db(query, data)
	if friends:
		flash("Log In Scuccessful");
	else:
		flash("Email or password is incorrect");
	return redirect('/')

app.run(debug=True)