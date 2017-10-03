from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
@app.route('/')
def no_ninja():
  return render_template("nonin.html")

@app.route('/ninja/<color>')
def show(color):
    ninjas = {
        'orange':'michelangelo',
        'blue':'leonardo',
        'red':'raphael',
        'purple':'donatello'
    }
    
    if color in ninjas:
        character = ninjas[color]
    else:
        character = 'notapril'
    return render_template('ninja.html', character=character)


app.run(debug=True)