# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/register', methods=['POST'])
def submit():
	email = request.form['email'];
	firstN = request.form['first'];
	lastN = request.form['last'];
	pwd = request.form['password'];
	pwdCon = request.form['password2'];

	errors = False;
	print errors
	if len(email) < 1:
		flash("Email cannot be blank!")
		errors = True;
	if len(firstN) < 1:
		flash("First Name cannot be blank!")
		errors = True;
	if len(lastN) < 1:
		flash("Last Name cannot be blank!")
		errors = True;
	if len(pwd) < 1:
		flash("Password cannot be blank!")
		errors = True;
	if len(pwdCon) < 1:
		flash("Confirm Password cannot be blank!")
		errors = True;
	if not EMAIL_REGEX.match(email):
		flash("Invalid Email Address!")
		errors = True;
	if not firstN.isalpha() or not lastN.isalpha():
		flash("First and last name should not comtain number(s)")
		errors = True;
	if len(pwd) < 8:
		flash("Password should not be less than 8 characters")
		errors = True;
	if pwd != pwdCon:
		flash("Password and Confirm Password are not match")
		errors = True;
	if not errors:
		flash("Thanks for submitting your information")
	return redirect('/')

app.run(debug=True)