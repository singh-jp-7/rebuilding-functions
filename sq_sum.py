# Function to return the sum of squares of all the positive integer smaller than a positive integer n.

def sq_sum(n):
	x = [i*i for i in range(1,n)]
	return sum(x)


print sq_sum(4)
