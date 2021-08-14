# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	# Your code goes here
	for i in range(len(a)):
		if(len(a)!=len(a[i])):
			return False
	if(len(a)==1):
		return True
	s=[]
	for i in range(len(a)):
		s.append(sum(a[i]))
	if(len(set(s))!=1):
		return False
	cs=0
	for i in range(len(a[0])):
		for j in range(len(a)):
			cs+=a[j][i]
		s.append(cs)
		cs=0
	if(len(set(s))!=1):
		return False
	ds=0
	for i in range(len(a)):
		for j in range(len(a[0])):
			if(i==j):
				ds+=a[i][j]
	s.append(ds)
	ds=0
	ds1=0
	if(len(set(s))!=1):
		return False
	for i in range(len(a)):
		for j in range(len(a[0])):
			if((i+j)==(len(a)-1)):
				ds1+=a[i][j]
	s.append(ds1)
	ds1=0
	if(len(set(s))!=1):
		return False
	return True