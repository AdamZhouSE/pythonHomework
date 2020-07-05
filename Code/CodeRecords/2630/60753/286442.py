import sys
import re
import heapq
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
nsq=len(nums)
n=int(nsq**0.5)
seen={(0,0)}
hp=[(nums[0],0,0)]
ans=0
while hp:
    d,x,y=heapq.heappop(hp)
    ans=max(ans,d)
    if x==y==n-1:
        print(ans)
    else:
        for xi,yi in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=xi< n and 0<=yi<n and (xi,yi) not in seen:
                heapq.heappush(hp,(nums[n*xi+yi],xi,yi))
                seen.add((xi,yi))
        
