import os

#Where every input is stored
tictactoelist=['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|']
choiceslist=['1','2','3','4','5','6','7','8','9']
inp1="1"
inp2="2"
X='|X|'
O='|O|'
ls='|_|'

#Prints the interface
def printit():
	os.system('clear')
	print(tictactoelist[0], tictactoelist[1], tictactoelist[2])
	print(tictactoelist[3], tictactoelist[4], tictactoelist[5])
	print(tictactoelist[6], tictactoelist[7], tictactoelist[8]) 

	choices()

#shows the choices available
def choices():
	print('\n')
	print(choiceslist[0], choiceslist[1], choiceslist[2])
	print(choiceslist[3], choiceslist[4], choiceslist[5])
	print(choiceslist[6], choiceslist[7], choiceslist[8]) 



#Inserts Xs to list
def insertX():

	global inp1
	del tictactoelist[inp1-1]
	tictactoelist.insert(inp1-1,X)
	del choiceslist[inp1-1]
	choiceslist.insert(inp1-1,'_')

#Inserts Os to list
def insertO():	
	global inp2
	del tictactoelist[inp2-1]
	tictactoelist.insert(inp2-1,O)
	del choiceslist[inp2-1]
	choiceslist.insert(inp2-1,'_')
	
def overwritecheck():
	pass

def gamewinX():
	if (tictactoelist[0]==X and tictactoelist[1]==X and tictactoelist[2]==X) or (tictactoelist[3]==X and tictactoelist[4]==X and tictactoelist[5]==X) or (tictactoelist[6]==X and tictactoelist[7]==X and tictactoelist[8]==X) or (tictactoelist[0]==X and tictactoelist[3]==X and tictactoelist[6]==X) or (tictactoelist[1]==X and tictactoelist[4]==X and tictactoelist[7]==X) or (tictactoelist[2]==X and tictactoelist[5]==X and tictactoelist[8]==X) or (tictactoelist[0]==X and tictactoelist[4]==X and tictactoelist[8]==X) or (tictactoelist[6]==X and tictactoelist[4]==X and tictactoelist[2]==X):
		os.system('clear')
		print("\n\nPLAYER 1 HAS WON!!\n\n")
		quit()

def gamewinO():
	if (tictactoelist[0]==O and tictactoelist[1]==O and tictactoelist[2]==O) or (tictactoelist[3]==O and tictactoelist[4]==O and tictactoelist[5]==O) or (tictactoelist[6]==O and tictactoelist[7]==O and tictactoelist[8]==O) or (tictactoelist[0]==O and tictactoelist[3]==O and tictactoelist[6]==O) or (tictactoelist[1]==O and tictactoelist[4]==O and tictactoelist[7]==O) or (tictactoelist[2]==O and tictactoelist[5]==O and tictactoelist[8]==O) or (tictactoelist[0]==O and tictactoelist[4]==O and tictactoelist[8]==O) or (tictactoelist[6]==O and tictactoelist[4]==O and tictactoelist[2]==O):
		os.system('clear')
		print("\n\nPLAYER 2 HAS WON!!\n\n")
		quit()

def gamewin():
	if ls not in tictactoelist:
		os.system('clear')
		print("\n\nGAME DRAW\n\n")
		quit()

os.system('clear')
input("PLAYER 1 : X\nPLAYER 2 : O\nPlay with the NumPad\nPress any key to continue ...")


while True:
	

	printit()
	inp1=int(input("\nPLAYER 1 : Enter a number between 1-9: "))
	insertX()
	printit()
	gamewinX()
	gamewinO()
	gamewin()
	inp2=int(input("\nPLAYER 2 : Enter a number between 1-9: "))
	insertO()
	printit()
	gamewinX()
	gamewinO()
	gamewin()

