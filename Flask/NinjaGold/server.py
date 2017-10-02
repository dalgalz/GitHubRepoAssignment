from flask import Flask, render_template, request, redirect, session
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
  	return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def guess_num():
	if "act" not in session: 
		session["act"] = "";
	# The random module has many useful functions. This is one that gives a random number in a range
	building = request.form['building']
	if building == "farm":
		randomNum = random.randrange(10, 21)
		session["coin"] += randomNum;
		session["act"] += "<p class=\'earn\'>Earn " + str(randomNum) + " goals from " + building + "!</p><br>"
	elif building == "cave":
		randomNum = random.randrange(5, 11)
		session["coin"] += randomNum;
		session["act"] += "<p class='earn'>Earn " + str(randomNum) + " goals from " + building + "!</p><br>"
	elif building == "house":
		randomNum = random.randrange(2, 6)
		session["coin"] += randomNum;
		session["act"] += "<p class='earn'>Earn " + str(randomNum) + " goals from " + building + "!</p><br>"
	elif building == "casino":
		randomNum = random.randrange(-50, 51)
		session["coin"] += randomNum;
		if randomNum >= 0:
			session["act"] += "<p class='earn'>Earn " + str(randomNum) + " goals from " + building + "!</p><br>"
		elif randomNum < 0:
			session["act"] += "<p class='earn'>Lose " + str(abs(randomNum)) + " goals from " + building + "!</p><br>"
  	return redirect('/')

app.run(debug=True) # run our server