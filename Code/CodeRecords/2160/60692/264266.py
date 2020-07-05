dividend = int(input())
divisor = int(input())
q = 0
if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
    dividend, divisor = abs(dividend), abs(divisor)
    while dividend > divisor:
        dividend -= divisor
        q += 1
elif dividend == 0:
    if divisor == 0:
        print("除零错误")
else:
    if dividend > 0:
        while dividend >= abs(divisor) and dividend > 0:
            dividend += divisor
            q -= 1
    elif dividend < 0:
        while abs(dividend) >= divisor and dividend < 0:
            dividend += divisor
            q -= 1
print(q)