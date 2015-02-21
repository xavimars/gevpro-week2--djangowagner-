#!/usr/bin/env python
#Xavier Marseille


import sys

class Country:
	def __init__(self, country):
		self.country = country
		
	def __str__(self):
		greet = "Hello from" + " " + self.country +""
		return greet

def main(argv):
	land = Country(argv[1])
	print(land.__str__())
	
if __name__ == '__main__':
	main(sys.argv)
