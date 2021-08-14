# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	# Your code goes here
	if(a==[]):
		return []
	i=0
	arr=[]
	c=1
	if(len(set(a))==1):
		return([(len(a),a[0])])
	while(i<len(a)-1):
		if(a[i]==a[i+1]):
			c+=1
		else:
			arr.append((c,a[i]))
			c=1
		i+=1
	if(a[-1]!=a[-2]):
		arr.append((1,a[-1]))
	elif(a[-1]==a[-2]):
		arr.append((c,a[-1]))

	return arr

