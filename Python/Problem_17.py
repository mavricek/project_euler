# Euler Problem 17
# Number letter counts
# Count all the numbers from 1 - 1000


def calc_dig_2(num):
    singles = ['zero', 'one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']
    singles_2 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    doubles = ['zero', 'ten', 'twenty', 'thirty', 'forty',
               'fifty', 'sixty', 'seventy', 'eighty', 'ninty']

    num2 = str(num)

    if len(num2) == 1:
        return len(singles[num])

    else:
        dig_2 = num2[0]
        dig_1 = num2[1]
        if num < 20:
            return len(singles_2[int(dig_1)])
        elif num % 10 == 0:
            return len(doubles[int(dig_1)])
        else:
            return len(doubles[int(dig_2)]) + len(singles[int(dig_1)])


def calc_digs(num):
    hundreds = ['zero', 'onehundred', 'twohundred', 'threehundred', 'fourhundred',
                'fivehundred', 'sixhundred', 'sevenhundred', 'eighthundred', 'ninehundred']
    num2 = str(num)

    if len(num2) < 3:
        return calc_dig_2(num)

    elif len(num2) == 3:
        dig_3 = num2[0]
        dig_2 = num2[1]
        dig_1 = num2[2]

        if num % 100 == 0:
            return len(hundreds[int(dig_3)])
        else:
			return len(hundreds[int(dig_3)]) + 3 + calc_dig_2(int(num2[1:]))
    else:
        return len('onethousand')


def main():
    tot = 0
    x = 1
    y = 1000

    for i in range(x, y + 1):
        print 'Letter count of %s is %s' % (i, calc_digs(i))
        tot += calc_digs(i)

    print 'For %s to %s the total letter count is %s' % (x, y, tot)

main()
