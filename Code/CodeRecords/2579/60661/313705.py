n=eval(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().strip().split(','))))
threshold=eval(input())
m=len(matrix[0])
maxl=0
l=min(m,n)
for i in range(n):
    for j in range(m):
        templ=0
        tempi=i
        tempj=j
        temp=0
        while temp<=threshold:
            temp=0
            if (tempi+1<=n)&(tempj+1<=m):
                tempi+=1
                tempj+=1
                for i1 in range(i,tempi):
                    for j1 in range(j,tempj):
                        temp+=matrix[i1][j1]
                if temp<=threshold:
                    templ+=1
            else:
                break
        maxl=max(maxl,templ)
print(maxl)