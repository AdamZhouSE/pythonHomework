n = int(input())
if not n:
    print(1)
else:
    res, muls = 10, 9
    for i in range(1, min(n, 10)):
        muls *= 10 - i
        res += muls
    print(res)
