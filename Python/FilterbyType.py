sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

#The number is big or small
def isBigorSmall(i):
	if i < 100:
		print "That's a small number"
	else:
		print "That's a big number!"
	return

isBigorSmall(sI);
isBigorSmall(mI);
isBigorSmall(bI);
isBigorSmall(eI);
isBigorSmall(spI);

#The sentense is short or small
def isShortorLong(s):
	if len(s) < 50:
		print "Short Sentense"
	else:
		print "Long Sentense"
	return

isShortorLong(sS);
isShortorLong(mS);
isShortorLong(bS);
isShortorLong(eS);

def isGreatorLess(l):
	if len(l) < 10:
		print "Short List"
	else:
		print "Long List"
	return

isGreatorLess(aL);
isGreatorLess(mL)
isGreatorLess(lL)
isGreatorLess(eL)
isGreatorLess(spL)