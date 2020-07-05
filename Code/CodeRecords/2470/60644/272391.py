g=int(input())
for k in range(0,g):
    n=int(input())
    a=input().split()
    for i in range(0,n*n):
        a[i]=int(a[i])
    r=[]
    for i in range(0,n):
        arr=[]
        for j in range(0,n):
            arr=arr+[a[i*n+j]]
        r=r+[arr]
    for i in range(0,n):
        for j in range(i,n):
            r[i][j],r[j][i]=r[j][i],r[i][j]
    res=''
    for i in range(0,n):
        for j in range(0,n):
            res=res+' '+str(r[i][n-1-j])
    print(res[1:]+' ')

