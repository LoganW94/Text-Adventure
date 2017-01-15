import json

class Room:
	'handles rooom info, switching, and descriptions'
	__roomNumber = 0
	__roomDictionary = {}
	 

	def __init__(self):
		self.__roomDictionary = self.loadRoom()
		print(self.__roomDictionary['description'])

	def loadRoom(self):
		'loads current room from file and stores in dictionary'
		'refresh to print updated room'	
		
		filename = "%s.json" % str(self.__roomNumber)
		with open(filename, "r") as f:
			text = f.read()
			d = json.loads(text)
			f.close

		return d

	def getPrompt(self):
		prompt = self.__roomDictionary["prompt"]
		return prompt

	def currentRoom(self):
		'returns current room number'
		print("The current room number is %d" % self.__roomNumber)

	def changeRoom(self, vector):
		print("change test")
		vc = vector