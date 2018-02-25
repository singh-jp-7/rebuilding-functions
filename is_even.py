def fib(n):
	if n == 1 or n == 2:
		return 1
	index = [0] * n
	index[0],index[1] = 1,1
	for i in range(2,n):	
		index[i] = index[i-1] + index[i-2]
	return index[n-1]

