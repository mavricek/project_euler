import numpy as np

# Get the first triangle number with 500 divisors

# Get the list of divisors
def div_count(x):
	divs = []
	for i in range(x+1):
		if(i > 0 and x%i == 0):
			divs.append(i)
	return len(divs)

# Get a method to create triangle numbers
def triangle(x):
	tri_x = 0
	for j in range(x+1):
		tri_x += j
	return tri_x

def main():
	x = 2400
	tri_x = triangle(x)
	divs = div_count(triangle(x))
	
	while divs <= 500:
		divs = div_count(tri_x)
		print 'Divider count for %s is %s' % (x, divs)
		x += 1 
		tri_x += x

	print 'Finished: triangle number of %s is %s with %s divisors' % (x, tri_x, div_count(tri_x))
	
main()

# Fina attempt interrupted at x = 3538