from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# our index route will handle rendering our form

@app.route('/')
def index():
	# The random module has many useful functions. This is one that gives a random number in a range
	if "coin" not in session: 
		session["coin"] = 0;
		session['act'] = []
  	return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def guess_num():
	time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")

	# The random module has many useful functions. This is one that gives a random number in a range
	building = request.form['building']
	if building == "farm":
		randomNum = random.randrange(10, 21)
		session["coin"] += randomNum;
		session["act"].append({'activity':"Earned {} golds".format(randomNum), 'class':'earn', 'date':time})
	elif building == "cave":
		randomNum = random.randrange(5, 11)
		session["coin"] += randomNum;
		session["act"].append({'activity':"Earned {} golds".format(randomNum), 'class':'earn', 'date':time})
	elif building == "house":
		randomNum = random.randrange(2, 6)
		session["coin"] += randomNum;
		session["act"].append({'activity':"Earned {} golds".format(randomNum), 'class':'earn', 'date':time})
	elif building == "casino":
		randomNum = random.randrange(-50, 51)
		session["coin"] += randomNum;
		if randomNum >= 0:
			session["act"].append({'activity':"Earned {} golds".format(randomNum), 'class':'earn', 'date':time})
		elif randomNum < 0:
			session["act"].append({'activity':"Lose {} golds".format(abs(randomNum)), 'class':'lose', 'date':time})
  	return redirect('/')

app.run(debug=True) # run our server