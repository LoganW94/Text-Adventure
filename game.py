import json
import room
import self
import os

def start():
	rm = room.Room()
	clearScreen()
	rm.loadRoom()
	nm = setName(rm)
	plr = self.Self(nm)
	plr.printInventory()

def clearScreen():
	os.system('clear')	

def setName(rm):
	prompt = rm.getPrompt()
	nm = input("%s" % prompt)	
	return nm

start()