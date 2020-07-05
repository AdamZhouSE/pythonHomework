num = int(input())
for j in range(num):
    n = int(input())
    res = 0
    for i in range(1, n + 1):
        temp = (i + 1) * (i) // 2
        res += temp
    print(res)
