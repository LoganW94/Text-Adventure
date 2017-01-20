import json
import textwrap

class Room:
	'handles rooom info, switching, and descriptions'

	def __init__(self):
		self.roomNumber = 0
		self.roomDictionary = self.loadRoom()
		

	def loadRoom(self):
		'loads current room from file and stores in dictionary'
		'refresh to print updated room'	
		filename = "%s.json" % str(self.roomNumber)
		with open(filename, "r") as f:
			text = f.read()
			d = json.loads(text)
			f.close
		return d

	def getPrompt(self):
		prompt = self.roomDictionary["prompt"]
		return prompt

	def currentRoom(self):
		'returns current room name'
		print("The current room is %s" % self.roomDictionary["name"])

	def changeRoom(self):
		self.roomNumber += 1
		print(self.roomNumber)
		self.roomDictionary = self.loadRoom()

	def printDescription(self):
		print("\n    %s" % textwrap.fill(self.roomDictionary['description']))	