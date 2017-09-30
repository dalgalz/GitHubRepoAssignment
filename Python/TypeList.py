#input
list1 = ['magical unicorns',19,'hello',98.98,'world']
list2 = [2,3,1,7,4,12]
list3 = ['magical','unicorns']

def typeList(listL):
	strL = ""
	sumL = 0
	for elm in listL:
		curr_type = type(elm)
		if curr_type is int:
			sumL += elm;
		elif curr_type is str:
			strL += " " + elm
	if sumL != 0 and strL != "":
		print "The list you entered is of mixed type"
		print "String:" + strL
		print "Sum:" , sumL
	elif sumL != 0:
		print "The list you entered is of integer type"
		print "Sum:" , sumL
	elif strL != "":
		print "The list you entered is of string type"
		print "String:" + strL
	return 

typeList(list1);
typeList(list2);
typeList(list3);

 