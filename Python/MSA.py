#print all the odd numbers from 1-1000
for i in range(1, 1000):
	if i % 2 == 1:
		print i
#print multiple of 5 from 5-1,000,000
for i in range(5, 1000):
	if i % 5 == 0:
		print i
#sum list
a = [1, 2, 5, 10, 255, 3]
x = 0
for l in a:
	x += l;
print x
#print avg a
print x/len(a)