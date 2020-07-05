x=int(input())
y=int(input())
bound=int(input())
res=[]
xexp,yexp=0,0
while x**xexp<=bound: xexp+=1
while y**yexp<=bound: yexp+=1

for i in range(xexp):
    for j in range(yexp):
        if x**i+y**j<=bound and x**i+y**j not in res: res.append(x**i+y**j)
        elif x**i+y**j>bound:break
res.sort()
print(res)
