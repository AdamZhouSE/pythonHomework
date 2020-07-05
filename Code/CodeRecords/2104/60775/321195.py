maxi = 200002
d = [0]*maxi
vis = [0]*maxi
det = [0]*maxi
ans = [maxi]
def dfs(i,k):
    global a
    vis[i] = k
    det[i] = 1
    if det[a[i]] == 0:
        dfs(a[i],k+1)
    if vis[a[i]] != 0 and vis[i] - vis[a[i]] +1 != 0:

        ans[0] = min(ans[0],vis[i]-vis[a[i]]+1)
    vis[i] = 0

n = int(input())
a = [int(x) for x in input().split(' ')]
a.insert(0,0)
for i in range(1,n+1):
    if det[i] == 0:
        dfs(i,1)
print(ans[0])
