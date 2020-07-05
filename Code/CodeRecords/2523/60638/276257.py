inpu=input()[1:-1].split("[")
mat=[]
for i in range(1,len(inpu)):
    if i==len(inpu)-1:
        mat.append(list(map(int, inpu[i][0:-1].split(","))))
    else:
        mat.append(list(map(int,inpu[i][0:-2].split(","))))
m=len(mat)
n=len(mat[0])
for i in range(0,m):
    temp=[]
    x=0
    y=i
    while x<n and y<m:
        temp.append(mat[y][x])
        x=x+1
        y=y+1
    temp.sort()
    x=0
    y=i
    while x<n and y<m:
        mat[y][x]=temp[x]
        x=x+1
        y=y+1
for i in range(1,n):
    temp=[]
    x=i
    y=0
    while x<n and y<m:
        temp.append(mat[y][x])
        x=x+1
        y=y+1
    temp.sort()
    x=i
    y=0
    while x<n and y<m:
        mat[y][x]=temp[y]
        x=x+1
        y=y+1
print(mat)