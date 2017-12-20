# Longest Collatz Sequence starting under 1M
# Collatz Sequence:
# If number is even, divide by two
# If number is odd, multiply by three and add one


def collatz(n):
    coll = []
    while n > 1:
        coll.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = n*3 + 1
    coll.append(1)
    return coll


def main():
    x = 999999
    x_coll = collatz(x)
    coll_len = len(x_coll)
    for i in range(x-1, 2, -1):
        i_coll = collatz(i)
        i_len = len(i_coll)
        if i_len > coll_len:
            coll_len = i_len
            print 'Collatz sequence for %s is %s long' % (i, i_len)

main()


