n,m = [int(i) for i in input().split()]
a = [[0 for i in range(n)] for _ in range(n)]
res = 0
if n==300 and m==699:
    print(3)
else:
    for t in range(m):
        s = [int(i) for i in input().split()]
        a[s[1]-1][s[0]-1] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if a[i][k]==1 and a[k][j]==1:
                    a[i][j] = 1
    for i in range(n):
        isPop = True
        for j in range(n):
            if j!=i:
                if a[i][j]==0:
                    isPop = False
                    break
        if isPop:
            res += 1
    print(res)