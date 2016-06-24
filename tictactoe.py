import os



#Where every input is stored
tictactoelist=[	]
inp1=""
inp2=""

#Prints the interface
def printit():
	os.system('clear')
	print(tictactoelist)

#Inserts elements to the list
def insert():

	global inp1
	global inp2	
	tictactoelist.insert(inp1-1,'X')
	
	if inp2==inp1:
		print("\nCannot Overwrite. Please enter another number: ")

	elif inp2!=inp1:
		tictactoelist.insert(inp2-1,'O')
	

while True:
	
	printit()
	inp1=input("\nPLAYER 1 : Enter a number between 1-9: ")
	insert()
	printit()
	inp2=input("\nPLAYER 2 : Enter a number between 1-9: ")
	insert()
	printit()
	
	