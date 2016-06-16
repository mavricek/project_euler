import numpy as np
from math import sqrt

# Get the first triangle number with 500 divisors

# Get the list of divisors
def div_count(x):
	divs = 0
	for i in range(1,int(x/2+1)):
		if(x%i == 0):
			divs += 1
	return divs + 1 #add one for x itself as factor

# Get a method to create triangle numbers
def triangle(x):
	tri_x = 0
	for j in range(x+1):
		tri_x += j
	return tri_x

def main():
	x = 6092
	tri_x = triangle(x)
	divs = div_count(triangle(x))

	while divs < 500:
		x += 1
		tri_x += x
		divs = div_count(tri_x)
		print 'Divider count of triangle number %s is %s' % (x, divs)

	print 'Finished: triangle number of %s is %s with %s divisors' % (x, tri_x, div_count(tri_x))

main()

# Last attempt interuppted at x = 6092
