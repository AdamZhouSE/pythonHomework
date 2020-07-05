divident = int(input())
divisor = int(input())
quotient = -1
if divident>0 and divisor>0:
    while divident>0:
        divident -= divisor
        quotient += 1
elif divident<0 and divisor<0:
    while divident<0:
        divident -= divisor
        quotient += 1
elif (divident>0 and divisor<0) or (divident<0 and divisor>0):
    divident = abs(divident)
    divisor = abs(divisor)
    while divident>0:
        divident -= divisor
        quotient += 1
    quotient = 0-quotient
else:
     m = 1
print(quotient)