row=[int(n) for n in input().split()]
n=row[0]
m=row[1]
all=0
xt=[]
for i in range(n):
    row1=[int(n) for n in input().split()]
    all+=row1[0]
    xt.append(row1[0]-row1[1])
num=0
xt.sort()
while all>m and len(xt)>0:
    all-=xt[len(xt)-1]
    xt.remove(xt[len(xt)-1])
    num+=1
if all>m:
    print(-1)
else:
    print(num)