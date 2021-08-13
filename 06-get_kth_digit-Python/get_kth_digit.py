# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	l=len(str(digit))
	if(k>=l):
		return 0
	else:
		if(digit<0):
			digit=-digit
		return (((digit%(10**(k+1)))-(digit%(10**(k))))//(10**k))
