import math

def adder(l):
    count = 0
    for i in range(len(l)):
        count += int(l[len(l) - 1 - i]) * int(math.pow(-2, len(l) - 1 - i))
    return count


def division(n):
    if n > 0:
        quotient = -1
        remainder = n - quotient * -2
        while remainder < 0 or remainder >= 2:
            quotient -= 1
            remainder = n - quotient * -2
    else:
        quotient = 1
        remainder = n - quotient * -2
        while remainder < 0 or remainder >= 2:
            quotient += 1
            remainder = n - quotient * -2

    s = str(quotient) + ',' + str(remainder)
    return s


l1 = input().split(',')
l2 = input().split(',')

n = adder(l1) + adder(l2)

if n == 1:
    print([1])
else:
    quotient = n
    l = []

    while int(division(quotient).split(',')[0]) != 1:
        l.append(int(division(quotient).split(',')[1]))
        quotient = int(division(quotient).split(',')[0])

    l.append(int(division(quotient).split(',')[1]))
    l.append(1)
    
    l.reverse()
    print(l)

