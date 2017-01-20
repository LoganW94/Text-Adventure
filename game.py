import json
import room
import player
import os
import interpret

def start():
	clearScreen()
	rm = room.Room()
	plr = player.Player()
	inter = interpret.Interpret()
	gameLoop(rm,plr, inter)

def clearScreen():
	os.system('clear')	

def gameLoop(rm, plr, inter):
	clearScreen()
	playing = True
	while playing == True:
		displayText(rm)
		plr_input = prompt().lower()
		inter.interpret(plr_input)
		if plr_input == "help":	
			print("\nyou cannot be helped")
		if plr_input == "go":
			rm.changeRoom()

def prompt():
	command = input("\nWhat will you do? ")
	return command

def displayLs(ls):
	for i in ls:
		print(i)

def displayText(rm):		
	rm.printDescription()

start()