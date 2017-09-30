import random
random_num = random.randint(60,100)

def score_grades(score):
	if score < 70:
		print "Score: ", score, "; Grade - D"
	elif score < 80:
		print "Score: ", score, "; Grade - C"
	elif score < 90:
		print "Score: ", score, "; Grade - B"
	elif score <= 100:
		print "Score: ", score, "; Grade - A"

score_grades(random_num);