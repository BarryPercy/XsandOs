###First Milestone Project. Tic Tac Toe
import random
import sys
from os import system
from IPython.display import clear_output
def checkifboardisfull(boardstate):
	counter = 0
	for i in boardstate:
		if i == 'X' or i=='O':
			counter+=1
	if counter==9:
		print("The game has ended in a draw!")
		sys.exit(0)
		return True
	else:
		return False

def hasplayerwon(shape,boardstate):
	playerhaswon=False
	if boardstate[0]==shape and boardstate[1]==shape and boardstate[2]==shape:
		playerhaswon=True
	elif boardstate[3]==shape and boardstate[4]==shape and boardstate[5]==shape:
		playerhaswon=True
	elif boardstate[6]==shape and boardstate[7]==shape and boardstate[8]==shape:
		playerhaswon=True
	elif boardstate[0]==shape and boardstate[3]==shape and boardstate[6]==shape:
		playerhaswon=True
	elif boardstate[1]==shape and boardstate[4]==shape and boardstate[7]==shape:
		playerhaswon=True
	elif boardstate[2]==shape and boardstate[6]==shape and boardstate[8]==shape:
		playerhaswon=True
	elif boardstate[0]==shape and boardstate[4]==shape and boardstate[8]==shape:
		playerhaswon=True
	elif boardstate[2]==shape and boardstate[4]==shape and boardstate[6]==shape:
		playerhaswon=True
	return playerhaswon
def randomizestartingorder(name1='name1',name2='name2'):
	goingfirst=random.randint(0,1)
	if goingfirst==0:
		print ("{} you are going first".format(name1))
	else:
		print ("{} you are going first".format(name2))
	return(goingfirst)
def displayboard(boardstate):
	print(' '+boardstate[0]+'|'+boardstate[1]+'|'+boardstate[2])
	print('-------')
	print(' '+boardstate[3]+'|'+boardstate[4]+'|'+boardstate[5])
	print('-------')
	print(' '+boardstate[6]+'|'+boardstate[7]+'|'+boardstate[8])
def taketurn(name,shape,boardstate):
	print('{} please choose a square to place an {} in the range 1-9: '.format(name,shape), end = '')
	movenotcorrect=True
	while(movenotcorrect):
		playerinput=int(input())
		if playerinput not in range(1,10) or boardstate[playerinput-1] =='X' or boardstate[playerinput-1] =='O':
			print('Invalid move, please enter a number between 1-9 that does not already contain an X or O: ', end = '')
		else:
			boardstate[playerinput-1] = shape
			system('cls') 
			displayboard(boardstate)
			break
	return boardstate
def rungame():
	print("Welcome to Tic Tac Toe!")
	print("What are your Names?")
	print("Player one: ", end = '')
	player1name=input()
	print("Player two: ", end = '')
	player2name=input()
	print("Great! Nice to meet you {} and {}. {} you will be Xs and {} you will be Os".format(player1name,player2name,player1name,player2name))
	player1shape='X'
	player2shape='O'
	currentturn=randomizestartingorder(player1name,player2name)
	currentboardstate=['1','2','3','4','5','6','7','8','9']
	displayboard(currentboardstate)
	gamenotover=True
	while (gamenotover):
		checkifboardisfull(currentboardstate)
		if currentturn==0:
			currentboardstate=taketurn(player1name,player1shape,currentboardstate)
			if hasplayerwon(player1shape,currentboardstate):
				break
			currentturn=1
		else:
			currentboardstate=taketurn(player2name,player2shape,currentboardstate)
			if hasplayerwon(player2shape,currentboardstate):
				break
			currentturn=0
	if currentturn==0:
		print('Congratulations {}! You have won!'.format(player1name))
	else:
		print('Congratulations {}! You have won!'.format(player2name))
rungame()
