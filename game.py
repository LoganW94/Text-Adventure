import json
import room
import player
import os
import parser

def start():
	clearScreen()
	rm = room.Room()
	plr = player.Player()
	parse = parser.Parse()
	gameLoop(rm,plr)

def clearScreen():
	os.system('clear')	

def gameLoop(rm, plr):
	clearScreen()
	while playing == True:
		displayText(rm, plr)
		plr_input = prompt().lower()
		if plr_input == "QUIT" or plr_input == "EXIT":
			break
		if plr_input == "HELP":	
			print("you cannot be helped")
		if plr_input == "GO":
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