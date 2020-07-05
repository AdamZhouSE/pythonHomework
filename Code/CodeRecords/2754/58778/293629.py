matrix=eval(input())
l=0
m=len(matrix)
n=len(matrix[0])
for i in range(m):
    for j in range(n):
        if matrix[i][j]!=l:
            l=1
            break
    if(l==1):
        break
k=1
for i in range(m):
    for j in range(n):
        if matrix[i][j]!=k:
            k=0
            break
    if(k==0):
        break
if(k==1 or l==0):
    print(-1)
else:
    ma=[]
    for i in range(m):
        for j in range(n):
            if(matrix[i][j]==0):
                temp=[]
                for x in range(m):
                    for y in range(n):
                        if(matrix[x][y]==1):
                            temp.append(abs(x-i)+abs(y-j))
                ma.append(temp)
    mi=min(ma[0])
    for i in ma:
        if(min(i)>mi):
            mi=min(i)
    print(mi)