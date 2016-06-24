# import numpy as np
# from math import sqrt

# Get the first triangle number with 500 divisors


# Get the list of divisors
def div_count(x):
    # From this: http://stackoverflow.com/questions/9076336/how-do-you-implement-the-divisor-function-in-code
    divs = 0
    sqroot = int(x ** 0.5)
    for i in range(1, sqroot + 1):
        if x % i == 0:
            divs += 2  # both factor and N/factor
    if sqroot * sqroot == x:
        divs -= 1  # if sqroot is a factor then we counted it twice, so subtract 1
    return divs


# Get a method to create triangle numbers
def triangle(x):
    tri_x = 0
    for j in range(x + 1):
        tri_x += j
    return tri_x


def main():
    x = 5
    tri_x = triangle(x)
    divs = div_count(triangle(x))

    while divs < 500:
        x += 1
        tri_x += x
        divs = div_count(tri_x)
        print 'Divider count is %s and x is %s' % (divs, x)

    print 'Finished: triangle number of %s is %s with %s divisors' % (x, tri_x, div_count(tri_x))


main()


