# uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = "abcdefghijklmnopqrstuvwxyz"

def is_pangram(sentence):
	return len(set([c for c in sentence.lower() if c.isalpha()]))==26

print(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"))