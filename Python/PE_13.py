import numpy as np

file_in = 'Problem 13 grid.txt'
data = np.loadtxt(file_in)

sum = 0

for row in data:
    sum += row
    print row

sum_st = str(sum)

print sum_st[:11]
