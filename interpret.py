import json
import os

class Interpret:
	#'this class takes user input, extrapulates intent, and returns a relevent function'
	dictionary = {}

	def __init__(self):
		'loads dictionary with commands'
		filename = 'dictionary.json'
		with open(filename, "r") as f:
			text = f.read()
			d = json.loads(text)
			f.close
		self.dictionary = d
			

	def string_to_array(self, plr_input):
		'Breaks up input string and returnd array'
		print("string")	

	def find_part_of_speech(self, array):
		'Searches dictionary for each word and returns its part of speach'
		arr = array
				
	def interpret(self, plr_input):
		plr = plr_input
		arr = self.string_to_array(plr)

		if plr_input == "quit" or plr_input == "exit":
			self.endGame()

	def endGame(self):
		quit()