def divide(dividend, divisor):
    if dividend == 0: return 0
    if divisor == 0: return

    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    tmp = 0
    for i in range(32, -1, -1):
        if tmp + (divisor << i) <= dividend:
            tmp += divisor << i
            quotient |= 1 << i

    quotient *= sign
    if quotient < -(2 ** 31) or quotient > 2 ** 31 - 1:
        return 2 ** 31 - 1
    else:
        return quotient
dividend=int(input())
divisor=int(input())
print(divide(dividend,divisor))