black = " "
white = "*"

for i in range(0,8):
	line = ""
	for j in range(0,8):
		if (abs(i - j) % 2) == 0:
			line += white
		elif (abs( i - j ) % 2) == 1:
			line += black
	print line