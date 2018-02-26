#function to determine if there is a distinct pair of numbers in a sequence whose product is odd

def odd_prod(*n):
	x = [i for i in n if i%2 != 0]
	if len(x) > 1:
		return True
	else:
		return False
