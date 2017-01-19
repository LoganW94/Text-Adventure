import json


class Parse:
	'this class takes user input, extrapulates intent, and returns a relevent function'
	dictionary = {}

	def __init__(self):
		'loads dictionary with commands'
		filename = 'dictionary'
		with open(filename, "r") as f:
			text = f.read()
			d = json.loads(text)
			f.close
		self.dictionary = d
		print self.dictionary	

	def string_to_array(self, plr_input):
		'Breaks up input string and returnd array'	

	def find_part_of_speech(self, array):
		'Searches dictionary for each word and returns its part of speach'
		arr = array
				
	def run(self, plr_input):
		plr = plr_input
		arr = self.string_to_array(plr)
