# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []
for elm in word_list:
	if elm.find(char) != -1:
		new_list.append(elm)
# output
print new_list
