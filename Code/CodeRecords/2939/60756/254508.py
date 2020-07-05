import heapq
line=list(map(int,input().split()))
K=line[0]
M=line[1]
spq=[1]
s=[]
for i in range(K):
    num=heapq.heappop(spq)
    heapq.heappush(spq,num*2+1)
    heapq.heappush(spq,num*4+5)
    s.append(str(num))
print(''.join(s))
s=list(''.join(s))
pointL=0
pointR=M
x=0
ans=[]
while pointL<=pointR and pointR<len(s):
    for i in range(pointL,pointR+1):
        if int(s[i])>x:
            x=int(s[i])
            pointL=i+1
    ans.append(str(x))
    pointR+=1
    x=0
print(''.join(ans),end="")