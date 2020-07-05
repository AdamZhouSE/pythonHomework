def arr28():
    n=int(input())
    set=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(1)
        set.append(row)
    for i in range(1,n):
        for j in range(i,n):
            set[i][j]= set[i-1][j] + set[i][j-1]

        for j in range(i,n):
            set[j][i]=set[j-1][i]+set[j][i-1]


    print(set[n-1][n-1])
    return

arr28()