num=input().split(" ")
for i in range(len(num)):
    num[i]=int(num[i])
minarr=[]
maxarr=[]
l=num[1]
r=num[2]
m=1
n=1
for j in range(num[0]-l+1):
    minarr.append(1)
for k in range(l-1):
    minarr.append(2*m)
    m=2*m
min=sum(minarr)
if r>num[0]:p=num[0]
else:p=r
for l in range(p):
    maxarr.append(n)
    n=2*n
for d in range(num[0]-r):
    maxarr.append(int(n/2))
max=sum(maxarr)
print(str(min)+" "+str(max))