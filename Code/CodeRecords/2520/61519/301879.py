r=int(input())
c=int(input())
r0=int(input())
c0=int(input())
res=[]
for i in range(r):
    for j in range(c):
        res.append([i,j])
res.sort(key = lambda x : abs((x[0]-r0)) + abs((x[1]-c0)))
print(res)