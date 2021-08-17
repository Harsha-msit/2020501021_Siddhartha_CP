# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isPrime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def numSquareSum(n): 
	squareSum = 0
	while(n): 
		squareSum += (n % 10) * (n % 10)
		n = int(n / 10)
	return squareSum

def isHappynumber(n): 
	slow = n
	fast = n
	while(True):  
		slow = numSquareSum(slow)
		fast = numSquareSum(numSquareSum(fast))
		if(slow != fast): 
			continue
		else: 
			break
	return (slow == 1)

def isHappyPrime(n):
	if((isHappynumber(n)) and isPrime(n)):
		return True
	return False

def fun_nth_happy_prime(n):
	found = 0
	guess = 0
	while(found<=n):
		guess+=1
		if(isHappyPrime(guess)):
			found+=1
	return guess