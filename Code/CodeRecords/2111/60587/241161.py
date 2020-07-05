n = int(input())
res = 1
while n > 0:
    if res == 1:
        n -= 1
        res += 1
    else:
        tmp = res
        while tmp % 2 == 0:
            tmp /= 2
        while tmp % 3 == 0:
            tmp /= 3
        while tmp % 5 == 0:
            tmp /= 5
        if tmp == 1:
            n -= 1
        res += 1
print(res-1)
