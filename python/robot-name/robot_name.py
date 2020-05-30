import random
import string

class Robot:
	
	usedNames = []
	
	def __init__(self):
		self.name = self.generate_new_random_name()

	def generate_new_random_name(self):
		while True:
			name = self.random_name()
			if name not in self.usedNames:
				return name

	def random_name(self):
		return "".join(random.choices(string.ascii_uppercase,k=2)) + str(random.randrange(100,1000))

	def reset(self):
		self.usedNames.append(self.name)
		self.name = self.generate_new_random_name()