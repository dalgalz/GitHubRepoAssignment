from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# our index route will handle rendering our form

@app.route('/')
def index():
	if "counter" in session: 
		session["counter"]+=1
	else:
		session["counter"]=1
  	return render_template("index.html")

@app.route('/addTwo', methods=['POST'])
def add_two():
   session['counter'] += 1
   return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_counter():
   session['counter'] = 0
   return redirect('/')

app.run(debug=True) # run our server