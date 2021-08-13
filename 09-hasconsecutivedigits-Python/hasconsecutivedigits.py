# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	if(n<0):
		n=-n
	while(n>0):
		cur=n%10
		n=n//10
		pre=n%10
		if cur==pre:
			return True
	return False