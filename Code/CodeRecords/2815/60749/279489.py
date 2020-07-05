n=int(input())
nums=list(map(int,input().split(" ")))
count=0
res=[]
for h in nums:
    if h>0:
        count+=(h-1)
        res.append(1)
    elif h<0:
        count+=(-1-h)
        res.append(-1)
    else:
        count+=1
        res.append(0)
m=0
t=0
for h in res:
    if h==-1:
        m+=1
    if h==0:
        t+=1
if m%2==0:
    print(count)
else:
    if t>0:
        print(count)
    else:
        count+=2
        print(count)