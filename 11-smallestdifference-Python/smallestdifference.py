# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	if(len(a)==0):
		return -1
	a.sort()
	mind=abs(a[0]-a[1])
	for i in range(1,len(a)):
		d=abs(a[i]-a[i-1])
		if(d<mind):
			mind=d
	return mind