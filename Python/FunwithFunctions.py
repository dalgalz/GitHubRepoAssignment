def odd_even():
	for i in range(1,2001):
		if i % 2 == 0:
			print "Number is", i, ". This is an even number."
		else:
			print "Number is", i, ". This is an odd number."

odd_even();

def multiply( a, b):
	listA = []
	for elm in a:
		listA.append(elm * b)
	return listA

def layered_multiples(arr):
	aList = []
	for arrElm in arr:
		tempList = []
		for i in range(0, arrElm):
			tempList.append(1)
		aList.append(tempList)
	return aList


a = [2,4,10,16]
print multiply( a, 5)

b = [2 ,4 ,5]
x = layered_multiples(multiply(b,3))
print x

