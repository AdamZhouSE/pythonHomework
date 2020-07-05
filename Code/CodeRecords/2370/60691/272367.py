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


#print(division(-1).split(',')[1])


n = int(input())
quotient = n
l = []

while int(division(quotient).split(',')[0]) != 1:
    l.append(int(division(quotient).split(',')[1]))
    quotient = int(division(quotient).split(',')[0])
    #print(n)

l.append(int(division(quotient).split(',')[1]))
l.append(1)

s = ""
length = len(l)
for i in range(length):
    s += str(l[length - i - 1])

print(s)
