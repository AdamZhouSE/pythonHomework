def dfs(root:int,LT:dict,RT:dict,top:list,arr:list)->int:
    if root in LT:
        dfs(LT[root],LT,RT,top,arr)
        if arr[LT[root]]>=arr[root]:
            top[root]+=1
        top[root]+=top[LT[root]]
    if root in RT:
        dfs(RT[root],LT,RT,top,arr)
        if arr[RT[root]]<=arr[root]:
            top[root]+=1
        top[root]+=top[RT[root]]
    return top[root]

from collections import defaultdict
n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,-1)
LT=defaultdict(int)
RT=defaultdict(int)
for i in range(2,n+1):
    fa,ch=map(int,input().split())
    if ch==0:
        LT[fa]=i
    else:
        RT[fa]=i
top=dfs(1,LT,RT,[0 for i in range(n+1)],arr)
print(top)