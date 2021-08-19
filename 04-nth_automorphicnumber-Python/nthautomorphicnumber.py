# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def nthautomorphicnumbers(n):
	# Your code goes here
	found = 1
	guess = -1
	while(found<=n):
		guess+=1
		if(isAutomorphic(guess)):
			found+=1
	return guess

def isAutomorphic(n):
	sq=n*n
	l=len(str(n))
	x=sq%(10**l)
	return x==n