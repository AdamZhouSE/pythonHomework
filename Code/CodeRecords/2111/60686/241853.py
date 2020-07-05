n = int(input())
if n <= 1:
    print(n)
else:
    res = [1] * n
    i2, i3, i5 = 0, 0, 0
    for i in range(1, n):
        res[i] = min(res[i2] * 2, min(res[i3] * 3, res[i5] * 5))
        if res[i] == res[i2] * 2:
            i2 += 1
        if res[i] == res[i3] * 3:
            i3 += 1
        if res[i] == res[i5] * 5:
            i5 += 1
print(res[-1])
