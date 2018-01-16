# Euler Problem 17 v2
# Number letter counts
# Count all the numbers from 1 - 1000


def wordify(num):
    singles = ['zero', 'one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
             'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    doubles = ['zero', 'ten', 'twenty', 'thirty', 'forty',
               'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    onek = 'onethousand'

    num2 = str(num)

    if len(num2) == 1:
        return singles[num]
    elif len(num2) == 2:
        dig2 = int(num2[0])
        dig1 = int(num2[1])
        if num < 20:
            return teens[dig1]
        elif num % 10 == 0:
            return doubles[dig2]
        else:
            return doubles[dig2] + singles[dig1]
    elif len(num2) == 3:
        dig3 = int(num2[0])
        dig2 = int(num2[1])
        dig1 = int(num2[2])
        if num % 100 == 0:
            return singles[dig3] + 'hundred'
        elif num % 10 == 0:
            return singles[dig3] + 'hundredand' + doubles[dig2]
        elif dig2 == 0:
            return singles[dig3] + 'hundredand' + singles[dig1]
        elif dig2 == 1:
            return singles[dig3] + 'hundredand' + teens[dig1]
        else:
            return singles[dig3] + 'hundredand' + doubles[dig2] + singles[dig1]
    else:
        return onek


def main():
    tot = 0
    x = 1
    y = 1000

    for i in range(x, y + 1):
        word_i = wordify(i)
        print 'Wordify of %s is %s, length of %s' % (i, word_i, len(word_i))
        tot += len(word_i)

    print 'For %s to %s the total letter count is %s' % (x, y, tot)

main()
