numerator = int(input())
denominator = int(input())

sign = ''
if numerator * denominator < 0:
    sign = '-'
    numerator = -numerator

quotient = 0

integer = numerator // denominator

remainder = numerator % denominator

allRemainder = {remainder: 0}

numerator = remainder

decimal = ''

while numerator != 0:
    quotient = numerator * 10 // denominator
    remainder = numerator * 10 % denominator

    if remainder in allRemainder:
        index = allRemainder.get(remainder)
        decimal = decimal[:index] + '(' + decimal[index:] + str(quotient) + ')'
        break

    allRemainder[remainder] = len(decimal) + 1

    numerator = remainder

    decimal += str(quotient)

if decimal != '':
    ans = sign + str(integer) + '.' + decimal
else:
    ans = sign + str(integer)

print(ans)
