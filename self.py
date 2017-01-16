
class Self:

	__inventory = {"picture": 
		"In the Picture there is a Boy and a Girl. They are sitting on a park bench on a sunny fall day",
		"sword":
		"A cheap sword. Probably a toy"
		}

	__credits = 0

	__name = ""	

	def __init__(self, name):
		self.__name = name

	def printInventory(self):
		for i in self.__inventory:
			print(i)