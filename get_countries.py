def getCountry():
	
	with open('countries_list.txt', 'r') as infile: #open file
		for x in infile: #takes every line from the file
			x = x.rstrip('\n') #strips from the right so that there are no white spaces
			print (x)

getCountry()
