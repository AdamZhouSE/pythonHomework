n,m,k,ans = 0,0,0,0
mp = [[0 for i in range(255)] for j in range(255)]
vis = [0]*255
lin = [0]*255
tot =0
def dfs(u:int,lim:int):
    global tot,mp,vis,lin,n,m
    for i in range(1,m+1):
        if mp[u][i]<=lim and vis[i]!=tot:
            vis[i] = tot
            if (not lin[i]) or dfs(lin[i],lim):
                lin[i] = u
                return True
    return False

def check(x:int):
    global tot,ans,n,vis,lin
    vis = [0] * 255
    lin = [0] * 255
    tot = 1
    ans = 0
    for i in range(1,n+1):
        ans+=dfs(i,x)
        tot+=1
    return ans

line = input().split(' ')
n = int(line[0])
m = int(line[1])
k = int(line[2])
k = n - k + 1
lim = -1
for i in range(1,n+1):
    s = input().split(' ')
    for j in range(1,m+1):
        mp[i][j] = int(s[j-1])
        lim = max(lim,mp[i][j])
mid = 0
l = 1
r = lim
while l<r:
    mid = (l+r)//2
    if check(mid)>=k:
        r = mid
    else:
        l = mid+1
print(l)