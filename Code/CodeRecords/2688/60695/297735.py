def toB(a, n):
    res = ""
    while a > 0:
        if a % 2 == 0:
            res = "0" + res
        else:
            res = "1" + res
        a = a // 2
    if len(res) < n:
        for i in range(n - len(res)):
            res = "0" + res
    return res


t = int(input())
for i in range(t):
    n = int(input())
    a = input().split(" ")
    a = list(map(int, a))
    tar = int(input())
    res = 0
    for j in range(1, 2 ** n):
        subset = toB(j, n)
        sum = 0
        for k in range(n):
            if subset[n - k - 1] == "1":
                sum += a[k]
        if sum == tar:
            res += 1
    print(res)

