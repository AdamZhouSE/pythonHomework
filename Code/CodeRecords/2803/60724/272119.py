fir=input().split()
n=int(fir[0])
m=int(fir[1])
q = []
for i in range(n):
    q.append(list(map(int, input().rstrip().split())))
res=[0]*m
for j in range(n):
    k=q[j][0]
    for e in  range(k):
        res[q[j][e+1]-1]=1
if 0 in res:
    print("NO")
else:
    print("YES")