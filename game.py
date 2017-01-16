import json
import room
import self
import os

__playing = True
__commandls = {}

def start():
	clearScreen()
	rm = room.Room()
	plr = self.Self()
	gameLoop(rm,plr)

def clearScreen():
	os.system('clear')	

def gameLoop(rm, plr):
	clearScreen()
	__commandls = loadCommands()
	while __playing == True:
		displayText(rm, plr)
		command = prompt()
		command = command.upper()
		if command == "QUIT" or command == "EXIT":
			break
		if command == "HELP":	
			displayLs(__commandls)
		if command == "GO":
			rm.changeRoom()	
		interpret(command)

def prompt():
	command = input("\nWhat will you do? ")
	return command

def interpret(command):
	command = command.upper()
	print(command)

def loadCommands():
	with open("commands.txt", "r") as f:
		text = f.read()
		d = json.loads(text)
		f.close
	return d	

def displayLs(ls):
	for i in ls:
		print(i)

def displayText(rm, lr):		
	rm.printDescription()

start()