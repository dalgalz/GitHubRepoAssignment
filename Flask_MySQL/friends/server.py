from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfrienddb')

@app.route('/')
def index():
	friends = mysql.query_db("SELECT * FROM fullfrienddb")
	return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO fullfrienddb (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'], 
             'last_name':  request.form['last_name'],
             'email': request.form['email']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE fullfrienddb SET first_name = :first_name, last_name = :lname, email = :email, updated_at = NOW() WHERE id = :id"
    data = {
             'first_name': request.form['first_name'], 
             'lname':  request.form['lname'],
             'email': request.form['email'],
             'id': friend_id
           }

    print "Glad"
    print friend_id
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
	# Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
	query = "SELECT * FROM fullfrienddb WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
	data = {'specific_id': friend_id}
	print "Glad2"
	print friend_id
    # Run query with inserted data.
	friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
	return render_template('editfriend.html', one_friend=friends[0])

@app.route('/friends/<friend_id>/delete')
def delete(friend_id):
    query = "DELETE FROM fullfrienddb WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)