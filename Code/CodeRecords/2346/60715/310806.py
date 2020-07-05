T=int(input())
while  T>0:
    m,n=map(int,input().split())
    p = [int(n) for n in input().split()]
    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):
            mat[i].append(p[i*n+j])
    x = 0
    y = -1
    ynum = n
    xnum = m - 1
    len=0
    while len < m * n and ynum >= 0 and xnum >= 0:
        for i in range(ynum):
            if(len==m*n-1):
                y += 1
                print(mat[x][y],end=' \n')
                len+=1
            else:
                y += 1
                print(mat[x][y], end=' ')
                len += 1
        for i in range(xnum):
            if(len==m*n-1):
                x += 1
                print(mat[x][y],end=' \n')
                len+=1
            else:
                x += 1
                print(mat[x][y], end=' ')
                len += 1
        ynum -= 1
        xnum -= 1
        if xnum >= 0:
            for i in range(ynum):
                if(len==m*n-1):
                    y -= 1
                    print(mat[x][y], end=' \n')
                    len += 1
                else:
                    y -= 1
                    print(mat[x][y], end=' ')
                    len += 1
            ynum -= 1
        if ynum >= 0:
            for i in range(xnum):
                if(len==m*n-1):
                    x -= 1
                    print(mat[x][y], end=' \n')
                    len += 1
                else:
                    x -= 1
                    print(mat[x][y], end=' ')
                    len += 1
            xnum-=1
    T-=1