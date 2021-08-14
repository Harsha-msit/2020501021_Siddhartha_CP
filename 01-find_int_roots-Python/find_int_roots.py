# Write the function bonusFindIntRoots(a,b,c) that takes 
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that 
# the roots are all integers. Your function should return these 2 int roots 
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

import math
def fun_find_int_roots(a, b, c):
	p=((b*b)-(4*a*c))**0.5
	r1=(-b+p)/(2*a)
	r2=(-b-p)/(2*a)
	root1=min(r1,r2)
	root2=max(r1,r2)
	return root1,root2


