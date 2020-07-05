def dfs(index,s):
    if s<0:
        return 0
    if mem[index][s]!=-1:
        return mem[index][s]
    if s==0:
        mem[index][s]=1
        return 1
    if index==n:
        return 0
    mem[index][s]=dfs(index+1,s)+dfs(index+1,s-li[index])
    return mem[index][s]


t = int(input())
for i in range(t):
    n = int(input())
    li = [int(x) for x in input().split()]
    k = int(input())
    mem = [[-1 for i in range(k+1)] for i in range(n+1)]
    print(dfs(0,k))