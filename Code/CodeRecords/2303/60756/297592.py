def dfs(val:int,step:int,v:list,perm:list,Bin:int)->bool:
    if v[val]: return 0
    if step==Bin: return 1
    v[val]=1
    x1=(val<<1)&(Bin-1)
    x2=(val<<1|1)&(Bin-1)
    perm[step]=val&1
    if dfs(x1,step+1,v,perm,Bin) or dfs(x2,step+1,v,perm,Bin): return 1
    v[val]=0
    return 0

n=int(input())
Bin=1<<n
print("%d" %(Bin),end=' ')
v=[0 for i in range(Bin)]
perm=[0 for i in range(Bin)]
dfs(0,1,v,perm,Bin)
for i in range(1,n):
    print('0',end='')
for i in range(1,Bin-n+2):
    print("%d" %(perm[i]),end='')
print()