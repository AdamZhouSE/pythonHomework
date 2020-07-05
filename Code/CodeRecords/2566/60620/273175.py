n=int(input())
r=[]
for i in range(n):
    r.append(list(map(int,input().split(','))))
m=len(r)
n=len(r[0])
d=[[0]*n for i in range(m)]
d[-1][-1]=max(1,1-r[-1][-1])
for i in range(n-2,-1,-1):
    d[-1][i]=max(1,d[-1][i+1]-r[-1][i])
for i in range(m-2,-1,-1):
    d[i][-1]=max(1,d[i+1][-1]-r[i][-1])
for i in range(m-2,-1,-1):
    for j in range(n-2,-1,-1):
        d[i][j]=max(min(d[i][j+1],d[i+1][j])-r[i][j],1)
print(d[0][0])
             
      