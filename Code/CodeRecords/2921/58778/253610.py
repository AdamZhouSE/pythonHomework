s=input()
sl=s.split( )
m=int(sl[0])
n=int(sl[1])
d=int(sl[2])
matrix=[]
for i in range(m):
    t=input()
    tl=t.split( )
    for j in range(n):
        matrix.append(int(tl[j]))
x=0
c=[]
for i in range(m*n):
    c.append(matrix[i]%d)
if(max(c)!=min(c)):
    print(-1)
else:
    for i in range(m*n):
        matrix[i]=int(matrix[i]/d)
    matrix.sort()
    k=[]
    for i in matrix:
        c=0
        for j in matrix:
           c=c+abs(j-i)
        k.append(c)
    print(min(k))