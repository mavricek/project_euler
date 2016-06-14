import numpy as np

def main():
	file_in = 'Problem 11 grid.txt'
	data = np.loadtxt(file_in, delimiter = ' ')

	nrows = data.shape[0]
	ncols = data.shape[1]
	
	print 'Number of rows is %s, and columns is %s.' % (nrows, ncols)
	
	max = 0
	print 'Max initialized at %s' % max
	
	max_i = []
	max_a = 0
	
	for j in range(nrows):
		for i in range(ncols):
			if(i < ncols - 4): # Horizontal sum
				max_i.append(data[j][i] * data[j][i+1] * data[j][i+2] * data[j][i+3])
			
			if(j < nrows - 4): # Vertical Sum
				max_i.append(data[j][i] * data[j +1][i] * data[j+2][i] * data[j+3][i])
				
				if(i < ncols - 4): # Diagonal right sum
					max_i.append(data[j][i] * data[j +1][i+1] * data[j+2][i+2] * data[j+3][i+3])
					
				if(i > 3): # Diagonal left sum
					max_i.append(data[j][i] * data[j +1][i-1] * data[j+2][i-2] * data[j+3][i-3])
			
			#print 'Max is %s, with length %s' % (max_i, len(max_i))
			
			for max_a in max_i:
				if max_a > max : 
					max = max_a
					print 'Max is now %s' % max			
			
			max_i = []
			
	print 'Final Max is %s' % max

main()