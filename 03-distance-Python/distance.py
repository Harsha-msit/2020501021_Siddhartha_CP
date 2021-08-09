# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.


def fun_distance(x1, y1, x2, y2):
	# your code goes here
	x=(abs(x1-x2)**2)
	y=(abs(y1-y2)**2)
	d1=round(((x+y)**0.5))
	d2=(((x+y)**0.5))
	if(d1>d2):
		return (d1-1)
	return d1