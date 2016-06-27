import os
import random

#Declarations
tictactoelist=['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|']
choiceslist=[1,2,3,4,5,6,7,8,9]
inp1="1"
inp2="2"
inpcomp="3"
ls='|_|'

#Prints the interface
def printit():
	os.system('clear')
	print(tictactoelist[0], tictactoelist[1], tictactoelist[2])
	print(tictactoelist[3], tictactoelist[4], tictactoelist[5])
	print(tictactoelist[6], tictactoelist[7], tictactoelist[8]) 
	choices()

#Shows the choices available
def choices():
	print('\n')
	print(choiceslist[0], choiceslist[1], choiceslist[2])
	print(choiceslist[3], choiceslist[4], choiceslist[5])
	print(choiceslist[6], choiceslist[7], choiceslist[8]) 

#Inserts Xs to list
def insertX(inp1):
	del tictactoelist[inp1-1]
	tictactoelist.insert(inp1-1,X)
	del choiceslist[inp1-1]
	choiceslist.insert(inp1-1,'_')

#Inserts Os to list by computer
def insertComp():	
	inpcomp = random.choice([x for x in choiceslist if isinstance(x, int)])
	del tictactoelist[inpcomp-1]
	tictactoelist.insert(inpcomp-1,O)
	del choiceslist[inpcomp-1]
	choiceslist.insert(inpcomp-1,'_')

#Inserts Os to list by player 2
def insertO(inp2):	
	del tictactoelist[inp2-1]
	tictactoelist.insert(inp2-1,O)
	del choiceslist[inp2-1]
	choiceslist.insert(inp2-1,'_')

#If X wins the game
def gamewinX():
	if (tictactoelist[0]==X and tictactoelist[1]==X and tictactoelist[2]==X) or (tictactoelist[3]==X and tictactoelist[4]==X and tictactoelist[5]==X) or (tictactoelist[6]==X and tictactoelist[7]==X and tictactoelist[8]==X) or (tictactoelist[0]==X and tictactoelist[3]==X and tictactoelist[6]==X) or (tictactoelist[1]==X and tictactoelist[4]==X and tictactoelist[7]==X) or (tictactoelist[2]==X and tictactoelist[5]==X and tictactoelist[8]==X) or (tictactoelist[0]==X and tictactoelist[4]==X and tictactoelist[8]==X) or (tictactoelist[6]==X and tictactoelist[4]==X and tictactoelist[2]==X):
		os.system('clear')
		print("\n\n"+X+" has WON!!\n\n")
		print(tictactoelist[0], tictactoelist[1], tictactoelist[2])
		print(tictactoelist[3], tictactoelist[4], tictactoelist[5])
		print(tictactoelist[6], tictactoelist[7], tictactoelist[8])
		print('\n')
		quit()

#If O wins the game
def gamewinO():
	if (tictactoelist[0]==O and tictactoelist[1]==O and tictactoelist[2]==O) or (tictactoelist[3]==O and tictactoelist[4]==O and tictactoelist[5]==O) or (tictactoelist[6]==O and tictactoelist[7]==O and tictactoelist[8]==O) or (tictactoelist[0]==O and tictactoelist[3]==O and tictactoelist[6]==O) or (tictactoelist[1]==O and tictactoelist[4]==O and tictactoelist[7]==O) or (tictactoelist[2]==O and tictactoelist[5]==O and tictactoelist[8]==O) or (tictactoelist[0]==O and tictactoelist[4]==O and tictactoelist[8]==O) or (tictactoelist[6]==O and tictactoelist[4]==O and tictactoelist[2]==O):
		os.system('clear')
		print("\n\n"+O+" has Won!!\n\n")
		print(tictactoelist[0], tictactoelist[1], tictactoelist[2])
		print(tictactoelist[3], tictactoelist[4], tictactoelist[5])
		print(tictactoelist[6], tictactoelist[7], tictactoelist[8])
		print('\n')
		quit()

#If X wins the game
def gamedraw():
	if ls not in tictactoelist:
		os.system('clear')
		print("\n\nGAME DRAW\n\n")
		print(tictactoelist[0], tictactoelist[1], tictactoelist[2])
		print(tictactoelist[3], tictactoelist[4], tictactoelist[5])
		print(tictactoelist[6], tictactoelist[7], tictactoelist[8])
		print('\n')
		quit()

#One Player mode
def oneplayer():
	os.system('clear')
	playerinp=input("Choose a Number : \n\n1) X\n2) O\n\n")

	while True:
		if playerinp=='1':
			X='|X|'
			O='|O|'
			break
		elif playerinp=='2':
			X='|O|'
			O='|X|'
			break
		else:
			os.system('clear')
			playerinp=input("Please enter a valid number : \n\n1) X\n2) O\n")

	global X
	global O
	input("\nPlay with the NumPad\nPress any key to continue ...")

	while True:
		printit()
		inp1=int(input("\nEnter a number : "))
		while True:
			if inp1 not in choiceslist:
				inp1=int(input("\nEnter a number from the choices given : "))
			else:
				break

		insertX(inp1)
		printit()
		gamewinX()
		gamewinO()
		gamedraw()
		insertComp()
		printit()
		gamewinX()
		gamewinO()
		gamedraw()

#Two Player mode
def twoplayer():
	os.system('clear')
	input("PLAYER 1 : X\nPLAYER 2 : O\n\nPlay with the NumPad\nPress Enter to continue ...")
	X="|X|"
	global X
	O="|O|"
	global O

	while True:
		printit()
		inp1=int(input("\nPLAYER 1 : Enter a number : "))
		while True:
			if inp1 not in choiceslist:
				inp1=int(input("\nEnter a number from the choices given : "))
			else:
				break

		insertX(inp1)
		printit()
		gamewinX()
		gamewinO()
		gamedraw()
		inp2=int(input("\nPLAYER 2 : Enter a number : "))

		while True:
			if inp2 not in choiceslist:
				inp2=int(input("\nEnter a number from the choices given : "))
			else:
				break

		insertO(inp2)
		printit()
		gamewinX()
		gamewinO()
		gamedraw()

#Main
os.system('clear')
print("TIC-TAC-TOE\n")
playerinp=input("Choose a Number : \n\n1)One Player \n2)Two Player \n\n")

while True:
	if playerinp=='1':
		oneplayer()
		break
	elif playerinp=='2':
		twoplayer()
		break
	else:
		os.system('clear')
		playerinp=input("Please enter a valid number : \n1)One Player \n2)Two Player \n\n")
		