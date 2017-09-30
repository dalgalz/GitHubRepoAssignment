x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(aList):
	for elm in aList:
		typeElm = type(elm)
		if typeElm is int:
			print "*" * elm
		elif typeElm is str:
			print elm[0].lower() * len(elm) 

draw_stars(x)
draw_stars(y)