from collections import defaultdict
N,K=tuple(map(int,input().split()))
fence=defaultdict(int)
cow=0
for i in range(N):
    line=input().split()
    L=int(line[0])
    direct=line[1]
    if direct=="R":
        for j in range(cow-L+1,cow+1):
            fence[j]+=1
        cow-=L
    else:
        for j in range(cow+1,cow+L+1):
            fence[j]+=1
        cow+=L
ans=0
for value in fence.values():
    if value>=K:
        ans+=1
print(ans,end="")