
class Self:

	inventory = {"picture": 
		"In the Picture there is a Boy and a Girl. They are sitting on a park bench on a sunny fall day",
		"sword":
		"A cheap sword. Probably a toy"
		}

	def __init__(self, name):
		self.name = name

	def printInventory(self):
		for i in self.inventory:
			print(i)