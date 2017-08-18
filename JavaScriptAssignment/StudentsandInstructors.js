var students = [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]

for ( var student in students)
{
	console.log(students[student].first_name + " " + students[student].last_name);
}

var users = {
 'Students': [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

for (var user in users)
{
	console.log(user);
 	for ( var person in users[user] )
 	{
 		console.log(users[user].indexOf(users[user][person]) + 1 + " - " + users[user][person].first_name.toUpperCase() + " " + users[user][person].last_name.toUpperCase() + " - " + (users[user][person].first_name.length + users[user][person].last_name.length));
 	}
}

