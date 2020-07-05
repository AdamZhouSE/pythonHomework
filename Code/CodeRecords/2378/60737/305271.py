inf=9999999
max1, summ = 0, 0
e, minn = [[0 for i in range(101)] for i in range(101)], [int('0x7f', 16)]*101
u = [1]*101

if __name__ == "__main__":
    con = [int(i) for i in input().split( )]
    n, m = con[0], con[1]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                e[i][j] = 0
            else:
                e[i][j] = inf
    for i in range(m):
        cmd = [int(j) for j in input().split( )]
        a, b, c = cmd[0], cmd[1], cmd[2]
        e[a][b] = c
        e[b][a] = c
        max1 +=c 

    minn[1]=0
    for i in range(1, n+1):
        k=0
        for j in range(1, n+1):
            if u[j] and minn[j] < minn[k]:
                k = j
        u[k] = 0
        for j in range(1, n+1):
            if u[j] and e[k][j] < minn[j]:
                minn[j] = e[k][j]

    for i in range(1, n+1):
        summ += minn[i]
    print(max1-summ, end="")
