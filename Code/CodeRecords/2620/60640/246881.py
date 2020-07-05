t = int(input())
for i in range(0, t):
    n = int(input())
    res = 0
    for j in range(1, n+1):
        res += pow(j, 5)
    print(res)
