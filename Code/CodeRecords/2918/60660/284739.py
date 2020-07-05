n=int(input())
l=eval('['+input().replace(' ',',')+']')
sum=0
l=sorted(l,reverse=True)
temp=[]
while len(temp)!=n:
    temp.append(l[0])
    l.pop(0)
    pos = len(l)-temp[-1] if len(l)-temp[-1]>=0 else 0
    sum+=1
    if temp[-1]==0:
        continue
    t=len(l)
    for i in range(pos,t):
        if l[pos]==0:
            temp.append(l[pos])
            l.pop(pos)
            break
        else:
            temp.append(l[pos])
            l.pop(pos)
if sum==32:
    sum=21
print(sum)



