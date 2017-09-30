import random

def headsTails(num):
	heads = 0
	tails = 0
	for i in range(1,num+1):
		random_num = random.random()
		round_num = round(random_num)
		coin = "head"
		if round_num == 0:
			heads += 1
		elif round_num ==1:
			tails += 1
			coin = "tail"
		print "Attempt #", i ,": Throwing a coin... It's a " , coin, "! ... Got" , heads ,"head(s) so far and ", tails , "tail(s) so far"

headsTails(5000)