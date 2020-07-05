def bfs(x,y):
    que = [(x,y)]
    mp[x][y] = "0"
    while que:
        curx,cury = que.pop(0)
        for a,b in [(curx-1,cury),(curx,cury-1),(curx+1,cury),(curx,cury+1)]:
            if 0<=a<row and 0<=b<col and mp[a][b]=="1":
                mp[a][b]="0"
                que.append((a,b))


mp=[]
try:
    while True:
        mp.append(list(input()))
except EOFError:
    pass
row = len(mp)
col = len(mp[0])
sum = 0
for i in range(row):
    for j in range(col):
        if mp[i][j]=="1":
            bfs(i,j)
            sum+=1
print(sum)  