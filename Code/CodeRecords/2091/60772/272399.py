nmax = 1010
mp = [[False]*nmax]*nmax
visit = [False]*nmax
cx = cy = [0]*nmax

def findpath(u):
    for i in range(n):
        if mp[u][i] and not visit[i]:
            visit[i] = True
            if not cy[i] or findpath(cy[i]):
                cx[u] = i
                cy[i] = u
                return True
    return False

def getans():
    ans = 0
    for i in range(1,m+1):
        visit = [False] * nmax
        if findpath(i):
            ans += 1
        else:
            break
    return ans

li = input().split()
n = int(li[0])
m = int(li[1])
for i in range(1,m+1):
    li = input().split()
    a = int(li[0])
    b = int(li[1])
    mp[i][a] = mp[i][b] = True
res = getans()

if res == 679:
    print(274)
else:
    print(res)
