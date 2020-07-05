dividend = int(input())
divisor = int(input())

sign = False
if dividend < 0 and divisor < 0 or dividend > 0 and divisor > 0:
    sign = True

if dividend == 0:
    print(0)
if divisor == 0:
    print("#")
else:
    divedSign = dividend > 0
    result = 0
    while True:
        if sign:
            dividend -= divisor
        else:
            dividend += divisor
        if not divedSign and dividend >0 or divedSign and dividend <0:
            break
        if sign:
            result += 1
        else:
            result -= 1
    print(result)
        