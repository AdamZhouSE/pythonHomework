get=eval(input())
n=0
for i in get:
    for j in i:
        if j>n:
            n=j
matrix=[[0 for i in range(n+1)] for i in range(n+1)]
matrix2=[[0 for i in range(n+1)] for i in range(n+1)]
for i in get:
    matrix[i[1]][i[0]]=1
    matrix2[i[0]][i[1]]=1
conti=True
for i in range(n,-1,-1):
    if conti:
        if matrix[i].count(1)>1:
            for j in range(n,-1,-1):
                if matrix[i][j]==1:
                    allzero=True
                    for k in range(n+1):
                        if matrix[k][i]==1:
                            allzero=False
                            break
                    if(allzero):
                        print([j,i])
                        conti=False
                        break
if conti:
    visited=[]
    while True:
        getzero=False
        for i in range(n+1):
            if matrix[i].count(1)==0 and i not in visited:
                getzero=True
                visited.append(i)
                for j in range(n+1):
                    matrix[j][i]=0
        if not getzero:
            break
    for i in range(len(get)-1,-1,-1):
        if matrix[get[i][1]][get[i][0]]==1 and matrix2[get[i][1]].count(1)!=0:
            print(get[i])
            break