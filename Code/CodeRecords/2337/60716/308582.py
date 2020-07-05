#初步想法：通过能放炸弹的地点使用permutation来寻找满足炸弹互不炸到的最大可能值
#n,m = map(int,input().split())
#maps = list()
#for i in range(n):
#    strs = list(input())
#    maps.append(strs)
if(visited[u]):return False
    if(k==t-1):return True
    ans[k]=u&1
    visited[u]=True
    if(dfs((u<<1)&(t-1),k+1)):return True
    if(dfs((u<<1|1)&(t-1),k+1)):return True
    visited[u]=False
    return False

n = int(input())
t = 2**n
print(t,end=" ")
ans = [0 for i in range(t)]
visited = [False for i in range(t)]
dfs(0,0)
ans = [str(i) for i in ([0]*(n-1)+ans)[:t]]
print("".join(ans))