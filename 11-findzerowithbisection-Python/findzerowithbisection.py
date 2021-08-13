# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.

def findzerowithbisection(x, epsilon):
	# epsilon and step are initialized
	# don't change these values
	# epsilon
	# your code starts here
	l=1
	r=x
	while(l<r):
		m=(l+r)/2.0
		s=m*m
		if((s-x)>0 and (s-x)<=epsilon):
			return m
		elif((s-x)>epsilon):
			r=m
		elif((s-x)<epsilon):
			l=m

# def almEq(a,b):
# 	if(abs(a-b)<10**-14):
# 		return True
# 	return False