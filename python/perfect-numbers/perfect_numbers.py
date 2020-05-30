
def listOfFactors(n):
	return [i for i in range(1,(n//2)+1) if n%i == 0]


def classify(number):
	if number > 0:
		ans_sum = sum(listOfFactors(number))
		if ans_sum == number:
			return "perfect"
		if ans_sum > number:
			return "abundant"
		if ans_sum < number:
			return "deficient"
	else:
		raise Exception('Number should be > 0.')
		