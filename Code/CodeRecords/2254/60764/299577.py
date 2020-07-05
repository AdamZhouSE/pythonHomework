f,r=map(int,input().split())
matrix=[[0]*f for i in range(f)]
for i in range(r):
    path=list(map(int,input().split()))
    matrix[path[0]-1][path[1]-1]=1
    matrix[path[1]-1][path[0]-1]=1
res=0
for i in range(f):
    s=sum(matrix[i])
    if s<2:
        res=res+2-s
if res%2==0:
    res=int(res/2)
else:
    res=int(res/2)+1
print(res)