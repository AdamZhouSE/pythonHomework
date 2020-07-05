lst=input().split()
n=int(lst[0])
m=int(lst[1])
gra=[[0 for i in range(n)]for j in range(n)]
for i in range(m):
    list0=input().split()
    list0=list(map(int,list0))
    gra[list0[0]-1][list0[1]-1]=1
print(gra)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if gra[i][k]==1 and gra[k][j]==1:
                gra[i][j]=1


count=0
for i in range(n):
    isF=False
    for j in range(n):
        if gra[j][i]==0 and j!=i:
            isF=True
            break
    if not isF:
        count+=1
print(count)