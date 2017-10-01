my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dicInTupOut(my_dict):
	my_tuple = zip(my_dict.keys(),my_dict.values())
	print my_tuple

dicInTupOut(my_dict)