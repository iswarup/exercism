class Digits:
	def __init__(self,number):
		self.number = number

	def __str__(self):
		return str(self.number)

	def number0fDigits(self):
		self.count = 0
		if self.number == 0:
				self.count += 1
		else:
			while self.number != 0:
				self.number = self.number//10
				self.count += 1
		# self.number = 
		return self.count

	def listOfDigitsMethod(self,number):
		self.listOfDigits = []
		while number > 9:
			rem = number%10
			number = number//10
			self.listOfDigits.append(rem)
		self.listOfDigits.append(number)
		return self.listOfDigits

# def numberOfDigits(number):
# 	listOfDigits = []
# 	count = 0
# 	while number != 0:
# 		number = number//10
# 		listOfDigits.append(number%10)
# 		count += 1
# 	return count

# n = Digits(1583)
# print(n.number0fDigits())
# print(n.listOfDigitsMethod())

def is_armstrong_number(number):
	digit = Digits(number)
	# print(digit)

	n = digit.number0fDigits()
	# print(n)

	listofDigitsInNumber = digit.listOfDigitsMethod(number)
	# print(listofDigitsInNumber)

	ans = 0
	for i in listofDigitsInNumber:
		ans = ans + i ** n
	if ans != number:
		return False
	else:
		return True

# print(is_armstrong_number(153))
# armList = [i for i in range(1000000) if is_armstrong_number(i)]

# print(armList)