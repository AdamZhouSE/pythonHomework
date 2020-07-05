t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    res = 0
    for i in range(n-1):
        for j in range(i,n):
            if a[i]>a[j]:
                res += 1
    print(res)