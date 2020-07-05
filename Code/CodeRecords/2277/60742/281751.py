n = int(input())
k = int(input())
a = [[0 for i in range(k+1)] for _ in range(n+1)]
if n==0:
    print(a[n][k])
else:
    for i in range(k+1):
        a[1][i] = i
    for i in range(2,n+1):
        for j in range(1,k+1):
            minimum = j
            for x in range(1,j+1):
                minimum = min(minimum,1+max(a[i-1][x-1],a[i][j-x]))
            a[i][j] = minimum
    print(a[n][k])