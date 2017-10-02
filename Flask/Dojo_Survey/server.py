from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
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
   errors = False
   name = request.form['name']
   location = request.form['location']
   lang = request.form['lang']
   comment = request.form['comment']
   # redirects back to the '/' route
   if len(name) < 1:
      flash("Name cannot be empty!") # just pass a string to the flash function
      errors = True
   if len(comment) < 1:
      print "Hey"
      flash("comment cannot be empty!") # just pass a string to the flash function
      errors = True
   if len(comment) > 120:
      flash("Limit only 120 characters") # just pass a string to the flash function
      errors = True
   if errors:
      return redirect('/')
      
   return render_template("result.html" , name=name, location=location, lang=lang, comment=comment)

app.run(debug=True) # run our server
