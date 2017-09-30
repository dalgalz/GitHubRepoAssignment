words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
print words.replace("day","month", 1)

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0], y[len(y)-1]
z = [y[0], y[len(y)-1]]
print z

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
y = x[0:len(x)/2]
z = x[len(x)/2:len(x)-1]
z.insert(0, y)
print z