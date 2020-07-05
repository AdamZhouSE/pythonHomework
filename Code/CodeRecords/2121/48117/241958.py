n = int(input())

if n == 0:
    print(1)
else:
    res = 10
    mul = 9
    for i in range(1, min(n, 10)):
        mul *= 10 - i
        res += mul

print(res)