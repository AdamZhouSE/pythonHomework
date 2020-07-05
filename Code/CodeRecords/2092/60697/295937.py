import collections
import sys
size=int(input())
nums=list(map(int,input().split(' ')))
nums.insert(0,0)
N=210000
fa=[i for i in range(N)]
d=[0 for i in range(N)]
def findfa(x):
    global d,fa
    if(fa[x]!=x):
        xx=fa[x]
        fa[x]=findfa(fa[x])
        d[x]=d[x]+d[xx]
    return fa[x]

ans=sys.maxsize
for i in range(1,size+1):
    xx=findfa(i)
    yy=findfa(nums[i])
    if(xx==yy):
        ans=min(ans,d[i]+d[nums[i]]+1)
    else:
        fa[xx]=i
        d[xx]=d[i]
        fa[i]=nums[i]
        d[i]=1
print(ans,end='')




