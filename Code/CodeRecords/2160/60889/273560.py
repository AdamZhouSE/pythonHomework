dividend = int(input())
divisor = int(input())
isNeg = False
if divisor < 0:
    divisor = -divisor
    isNeg = not(isNeg)
if dividend < 0:
    dividend = -dividend
    isNeg = not(isNeg)
quotient = 0
while dividend>=divisor:
    dividend = dividend - divisor
    quotient = quotient + 1
if isNeg:
    quotient = -quotient
print(quotient)