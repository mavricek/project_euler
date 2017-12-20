# Project Euler no. 16
# Power digit sum

def main():
	pow = 1000
	num = 2 ** pow
	num_alph = str(num)
	print(num_alph)
	sum = 0
	for i in range(len(num_alph)):
		sum += int(num_alph[i])

	print 'Sum of all digits is %s' % sum

main()