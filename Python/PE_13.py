# Euler Problem #13
# Matej
# 2017 November 30

import numpy as np

def main():
	file_in = 'Problem 13 grid.txt'
	data = np.loadtxt(file_in)

	sum = 0

	for row in data:
	    sum += row
	    print row

	sum_st = str(sum)

	print sum_st[:11]

main()