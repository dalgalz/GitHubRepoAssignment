from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# our index route will handle rendering our form

@app.route('/')
def index():
	# The random module has many useful functions. This is one that gives a random number in a range
	if "randNum" not in session: 
		session['randNum'] = random.randrange(0, 101) # random number between 0-100
  	print session['randNum']
  	return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess_num():
	# The random module has many useful functions. This is one that gives a random number in a range
	guessNum = request.form['guess']
	print guessNum
	print session['randNum']
	if int(guessNum) < session['randNum']:
		session['hint'] = "low"
	elif int(guessNum) > session['randNum']:
		session['hint'] = "high"
	elif int(guessNum) == session['randNum']:
		session['hint'] = "correct"
  	return redirect('/')

@app.route('/reset')
def reset():
    session.pop('randNum')
    session.pop('hint')
    return redirect('/')


app.run(debug=True) # run our server