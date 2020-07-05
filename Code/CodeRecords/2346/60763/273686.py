def print2DArray(a):    #每次打印最外面一层
    if len(a[0]) == 1:
        for i in len(a):
            print(a[i][0],end=' ')
        return
    elif len(a) == 1 and len(a[0]) !=  1:
        for i in range(len(a[0])):
            print(a[0][i], end=' ')
    elif len(a) >1:
        row = len(a)
        col = len(a[0])
        i = 0
        while i < col:
            print(a[0][i], end=' ')
            i += 1
        i = 1
        while i < row:
            print(a[i][col-1], end=' ')
            i += 1
        i = col-2
        while i >= 0:
            print(a[row-1][i], end=' ')
            i -= 1
        i = row - 2
        while i >= 1:
            print(a[i][0], end=' ')
            i -= 1
        if row >2 and col >2:
            b = [[0 for i in range(col-2)] for j in range(row-2)]
            j = 1
            while j < row-1:
                k = 1
                while k < col-1:
                    b[j-1][k-1] = a[j][k]
                    k+=1
                j+=1
            print2DArray(b)

T = int(input())
for i in range(T):
    mn = list(map(int, ('' + input()).split(' ')))
    m, n = mn[0], mn[1]
    # print(m, n)
    mat = list(map(int, ('' + input()).split(' ')))
    # print(mat)
    a = [[0 for i in range(n)] for j in range(m)]  # m行n列
    count = 0
    for j in range(m):
        for k in range(n):
            # print(mat[j * m + k])
            a[j][k] = mat[count]
            count +=1
    # print(a)
    print2DArray(a)
    print()