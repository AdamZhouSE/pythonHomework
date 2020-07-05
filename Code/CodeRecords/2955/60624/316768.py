def func8():
    a = input().strip()
    b = input().strip()
    k = int(input())
    a1 = len(a)
    b1 = len(b)
    up = a1+b1
    low = max(a1,b1)
    g = [[0 for x in range(2020)] for x in range(2020)]
    for i in range(1,a1+1):
        g[i][0] = k+g[i-1][0]
    for i in range(1,b1+1):
        g[0][i] = k+g[0][i-1]

    temp = 0
    for i in range(1,a1+1):
        for j in range(1,b1+1):
            g[i][j] = k+g[i-1][j]
            temp = g[i][j-1]+k
            if temp < g[i][j]:
                g[i][j] = temp
            temp = g[i-1][j-1]+abs(ord(a[i-1])-ord(b[j-1]))
            if g[i][j] > temp:
                g[i][j] = temp
    print(g[a1][b1])
    return
func8()