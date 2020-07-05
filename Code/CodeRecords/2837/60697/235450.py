sizes=list(map(int,input().split(' ')))
num=sizes[0]
l=sizes[1]
r=sizes[2]
rmin=0
rmax=0
rres=[]
lres=[]
for i in range(num-l+1):
    rres.append(1)
for i in range(l-1):
    rres.append(1<<(i+1))
for k in rres:
    rmin=rmin+k
for i in range(r):
    lres.append(1<<(i))
for i in range(num-r):
    lres.append(1<<(r-1))
for k in lres:
    rmax=rmax+k
print(str(rmin),str(rmax))




