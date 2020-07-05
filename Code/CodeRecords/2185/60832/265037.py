import math

All = int(input())

for q in range(0, All):
    n = int(input())

    length = 1
    while n > math.pow(2, length + 1) - 2:
        length += 1

    t = n - int(math.pow(2, length) - 2)

    t -= 1
    ans = ''
    for i in range(length):
        if t % 2 == 0:
            ans = '4' + ans
        else:
            ans = '7' + ans
        t //= 2
    print(ans)