import json
import room
import self
import os

__playing = True

def start():
	clearScreen()
	rm = room.Room()
	rm.loadRoom()
	nm = setName(rm)
	plr = self.Self(nm)
	gameLoop()

def clearScreen():
	os.system('clear')	

def setName(rm):
	prompt = rm.getPrompt()
	nm = input("%s" % prompt)	
	return nm

def gameLoop():
	while __playing == True:
		clearScreen()
		rm.printDescription()
		command = prompt()

def prompt():
	command = input("What will you do? ")
	return command

start()