n=int(input())
matrix=[]
for i in range(n*n):
    s=input()
    sl=s.split()
    temp=[]
    temp.append(int(sl[0]))
    temp.append(int(sl[1]))
    matrix.append(temp)
matrix2=[]
re=[]
for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(0)
    matrix2.append(temp)
for i in range(n*n):
    x=matrix[i][0]
    y=matrix[i][1]
    if(matrix2[x-1][y-1]==0):
        for j in range(n):
            matrix2[x-1][j]=1
        for j in range(n):
            matrix2[j][y-1]=1
        re.append(i+1)
for i in range(len(re)):
    if(i!=len(re)-1):
        print(re[i],'',end='')
    else:
        print(re[i])
    