# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	s1=dist(x1, y1, x2, y2)
	s2=dist(x2, y2, x3, y3)
	s3=dist(x3, y3, x1, y1)
	ar=trianglearea(s1,s2,s3)
	return ar


def dist(x1,y1,x2,y2):
	x=(x2-x1)**2
	y=(y2-y1)**2
	d=(x+y)**0.5
	return d

def trianglearea(s1, s2, s3):
	# your code goes here
	s=(s1+s2+s3)/2
	return ((s*(s-s1)*(s-s2)*(s-s3))**0.5)