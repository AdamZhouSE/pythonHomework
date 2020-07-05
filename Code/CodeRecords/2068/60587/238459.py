dividend = int(input())  # 被除数
divisor = int(input())  # 除数
tmp = dividend
res = 0
if dividend == 0:
    print('0')
negative = (dividend ^ divisor) < 0
while True:
    if negative:
        dividend += divisor
        res -= 1
    else:
        dividend -= divisor
        res += 1
    if (dividend ^ tmp) < 0:
        break
if negative:
    res = res + 1
else:
    res = res - 1
print(res)
