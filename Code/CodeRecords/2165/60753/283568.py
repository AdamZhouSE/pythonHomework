import sys
import re
import math
import Queue
def bfs(node,start,ans,nums):
    visited=set()
    q=Queue.Queue()
    q.put(start)
    visited.add(start)
    while not q.empty():
        u=q.get()
        ans.append(u)
        indx=node.index(u)
        for i in range(n):
            if nums[n*indx+i]==1:
                t=node[i]
                if t not in visited:
                    visited.add(t)
                    q.put(t)
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
sli=s.split("\n")
T=nums[0]
del(nums[0])
n=nums[0]
del(nums[0])
del(sli[0])
line1=sli[0].split(" ")
del(sli[0])
start=line1[1]
node=[]
line2=sli[0].split(" ")
for ch in line2:
    node.append(ch)
ans=[]
bfs(node,start,ans,nums)
output=""
for i in range(len(ans)-1):
    output+=ans[i]+" "
output+=ans[-1]
print(output)

