#bfs
li=eval(input())
data = []
for i in range(len(li)):
    for j in range(len(li[0])):
        if li[i][j] == 1:
            data.append((i, j, 0))
        
d = [(0,1), (0,-1), (1,0), (-1,0)]
res = -1
while data:
    i,j,res = data.pop(0)
    for xd, yd in d:
        x, y = i + xd, j + yd
        if 0 <= x < len(li[0]) and 0 <= y < len(li) and li[x][y] == 0:
            li[x][y] = 1
            data.append((x, y, res+1))

if res==0:
    print(-1)
else:
    print(res)