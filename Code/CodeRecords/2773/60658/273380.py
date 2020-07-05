def dfs(x,y):
    if cache[x][y]!=0:
        return cache[x][y]
    for nx,ny in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]:
        if 0<=nx<n and 0<=ny<n and li[nx][ny]>li[x][y]:
            cache[x][y]=max(dfs(nx,ny),cache[x][y])
    cache[x][y]+=1
    return cache[x][y]

inp = input()
inp = input()
li = []
while inp!="]":
    # print(inp)
    if inp[-1]==',':
        inp = inp[:-1]
    li.append(eval(inp))
    inp = input()
# print(li)
n = len(li)
ans = -1
cache = [[0 for x in range(n)]for x in range(n)]
for i in range(n):
    for j in range(n):
        ans =max(ans,dfs(i,j))
print(ans)