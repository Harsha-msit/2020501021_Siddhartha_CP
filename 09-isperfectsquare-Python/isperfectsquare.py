# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

def isperfectsquare(n):
	# your code goes here
	if(type(n)==str):
		if(n.isnumeric()):
			n=int(n)
	if(type(n)!=int or n<0):
		return False
	if(n==1 or n==4):
		return True
	l=2
	h=(n//2)+1
	while(l<=h):
		m=l+((h-l)//2)
		if(m*m==n):
			return True
		if(m*m>n):
			h=m-1
		elif(m*m<n):
			l=m+1
	return False