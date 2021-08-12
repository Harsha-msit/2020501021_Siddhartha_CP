# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	mc=1
	o=0
	for i in range(9, -1, -1):
		c=countOccurrences(n, i)
		if(c>=mc):
			mc=c
			o=i
	return o


def countOccurrences(n, i): 
    c = 0               
    while (n):            
        if ((n%10)==i): 
            c=c+1 
        n = int(n/10)    
    return c