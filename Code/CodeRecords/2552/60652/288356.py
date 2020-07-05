
from collections import defaultdict
n,m=map(int,input().split())
l=defaultdict(list)
index=1
for i in range(m):
    Q,L,R=map(int,input().split())
    if Q==1:
        for j in range(L-1,R):
            l[j].append(index)
    else:
        MAX=0
        for j in range(L-1,R):
            MAX=max(MAX,len(l[j]))
        print(MAX)
