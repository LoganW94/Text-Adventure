import json
import room
import player
import os
import interpret

def start():
	clearScreen()
	rm = room.Room()
	plr = player.Player()
	inter = interpret.Interpret(rm)
	gameLoop(rm,plr, inter)

def clearScreen():
	os.system('clear')	

def gameLoop(rm, plr, inter):
	clearScreen()
	playing = True
	'main loop for the game. Includes flavor text print line, that should play only at entrance into room'
	while playing == True:
		same_room = True
		'displays the flavor text for the room'
		rm.printDescription()
		'game loop for player interactions in game'
		while same_room == True:
			plr_input = prompt().lower()
			inter.interpret(plr_input)
			
			

def prompt():
	command = input("\nWhat will you do? ")
	return command

def displayLs(ls):
	for i in ls:
		print(i)

start()