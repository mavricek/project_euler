# Lattice Paths
# IF you can move only right and down
# How many ways are there to move through a 20 x 20 grid
# THere are 6 ways to do this for a 2x2 grid


def main():
    x = 2
    paths = 0
    print range(0, x+1)
    for i in range(0, x+1):
        if i != x:
            paths += 2
        else:
            paths += 1

    print 'Total paths are %s' % paths

main()
