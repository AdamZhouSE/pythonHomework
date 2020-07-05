dividend = int(input())
divisor = int(input())
isNeg = False
if divisor < 0 <= dividend or dividend < 0 < divisor:
    isNeg = True
    if divisor < 0:
        divisor = -divisor
    else:
        dividend = -dividend
quotient = 0
while dividend >= divisor:
    dividend -= divisor
    quotient += 1
if isNeg:
    print(-quotient)
else:
    print((quotient))
