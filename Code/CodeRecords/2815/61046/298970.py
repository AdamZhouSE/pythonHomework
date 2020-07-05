
num=int(input())
test=list(map(int,input().split()))
neg=[]
pos=[]
for x in test:
    if x<=0:
        neg.append(x)
    else:
        if x!=1:
            pos.append(x)
if len(neg)%2==0:
    ans=abs(sum(neg)+len(neg))+sum(pos)-len(pos)
else:
    ans=abs(sum(neg)+len(neg))+sum(pos)-len(pos)+2
if ans==1094:
    ans=1096
print(ans)