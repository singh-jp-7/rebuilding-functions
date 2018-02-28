"""
The p-norm of a vector v = (v1, v2, v3,.....,vn) in n-dimensional space is defined as

				|v| = p_root(v1^p + v2^p + v3^p + ....+ vn^p)

For the special case of p = 2, this results in the traditional Euclidean norm, whicj represents the length of the vector.
Give an implementation of a function named norm such that norm(v,p) returns the p-norm value of v and norm(v) returns the Euclidean norm of v
"""
def norm(v,p=2):
	temp_ans = 0
	for i in v:
		temp_ans += i**p
	ans = 0
	low = 0
	high = max(1, abs(temp_ans))
	e = 0.01
	while abs(ans**p - temp_ans) > e:
		if ans**p > abs(temp_ans):
			high = ans
		else:
			low = ans
		ans = (low+high)/2.0
	if temp_ans < 0:
		return -1*ans
	else:
		return ans
