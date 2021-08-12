# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	d1=distsq(x1, y1, x2, y2)
	d2=distsq(x2, y2, x3, y3)
	d3=distsq(x3, y3, x1, y1)
	if((d1+d2==d3) or (d2+d3==d1) or (d3+d1==d2)):
		return True
	return False

def distsq(x1,y1,x2,y2):
	x=(x2-x1)**2
	y=(y2-y1)**2
	d=x+y
	return d