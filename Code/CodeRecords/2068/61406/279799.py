dividend = int(input())
divisor = int(input())
quotient = 0
if dividend>=0 and divisor>0:
    while dividend>=divisor:
        dividend = dividend-divisor
        quotient = quotient+1
elif dividend>=0 and divisor<0:
    while abs(dividend)>=abs(divisor):
        dividend = dividend+divisor
        quotient = quotient-1
elif dividend<0 and divisor>0:
    while abs(dividend)>=abs(divisor):
        dividend = dividend+divisor
        quotient = quotient-1
elif dividend<0 and divisor<0:
    while abs(dividend)>=abs(divisor):
        dividend = dividend-divisor
        quotient = quotient+1
print(quotient)