# Euler problem 8
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, Find the maximum total from top to bottom of the triangle below
# Matej
# 2018 Jan 16


def main():
    dir_git = "C:/Git/"
    file = dir_git + "project_euler/data/p18.txt"

    data = [[int(i) for i in line.split()] for line in open(file)]
    # print data

    bottom = data[len(data) - 1]
    # print bottom

    maxes = []
    max_tot = 0

    # The idea is to start from the bottom of the triangle, build the max adjecent path
    # Only for those bottom numbers greater than 50 (assuming the lower ones would be too low)
    # Let's start with position 3 for the first run

    # for j in range(0, len(bottom)):
    j = 2
    maxes_i = [bottom[j]]
    maxtot_i = 0
    pos = j
    print bottom[j]
    # if bottom[j] >= 50:
    for i in range(len(data) - 2, -1, -1):
        row = data[i]
        print row
        print row[pos:pos + j]
        if pos == 0:
            max_above = row[0]
        elif pos > len(row):
            max_above = row[len(row) - 1]
        else:
            max_above = max(row[pos - 1:pos])
        pos = row.index(max_above)
        print "Max above adjecent is %s at position %s" % (max_above, pos)
        maxes_i.append(max_above)
        maxtot_i += max_above

    if maxtot_i > max_tot:
        max_tot = maxtot_i
        maxes = maxes_i

    # print max1
    # print len(data)
    print "Max total is %s for  numbers: %s" % (max_tot, maxes)


main()
