
class Player:

	__inventory = {"picture": 
		"In the Picture there is a Boy and a Girl. They are sitting on a park bench on a sunny fall day",
		"sword":
		"A cheap sword. Probably a toy"
		}

	__credits = 0

	__name = ""	

	__location = 0

	

	def __init__(self):
		self.__name = "Default"

	def printInventory(self):
		for i in self.__inventory:
			print(i)

	def printCredits(self):
		print("You have %d credits" % self.__credits)

	def loadPlayer(self):
		print("loading")			