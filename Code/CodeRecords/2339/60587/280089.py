T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    num = input().split()
    res = 0
    for i in range(0, n - 1):
        for j in range(i, n):
            if int(num[j]) < int(num[i]):
                res += 1
    print(res)
