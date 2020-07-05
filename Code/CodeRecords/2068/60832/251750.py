dividend = int(input())
divisor = int(input())
ans = 0

if dividend > 0:
    if divisor < 0:
        temp = -divisor
        while temp < dividend:
            temp -= divisor
            ans -= 1
    else:
        temp = divisor
        while temp < dividend:
            temp += divisor
            ans += 1
else:
    if divisor > 0:
        temp = -divisor
        while temp > dividend:
            temp -= divisor
            ans -= 1
    else:
        temp = divisor
        while temp > dividend:
            temp += divisor
            ans += 1
print(ans)