from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/dojo', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   location = request.form['location']
   lang = request.form['lang']
   comment = request.form['comment']
   # redirects back to the '/' route
   return redirect('/result')

@app.route('/result')
def result():
  return render_template("result.html" , name=name, location=location, lang=lang, comment=comment)
app.run(debug=True) # run our server
