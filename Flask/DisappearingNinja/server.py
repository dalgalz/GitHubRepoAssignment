from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
@app.route('/')
def no_ninja():
  return render_template("nonin.html")

@app.route('/ninja')
def ninja():
  return render_template("ninja.html")

app.run(debug=True)