def valid(x,y):
    return 0<=x<len(lst) and 0<=y<len(lst[0]) and notVisited[x][y]

def bfs(x,y):
    q = [[x,y]]
    step = 0
    while q:
        ql = len(q)
        while ql>0:
            ql-=1
            begin = q.pop(0)
            x,y = begin[0],begin[1]
            if lst[x][y] == 1:
                return step
            notVisited[x][y] = False
            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx,ny = x+dx,y+dy
                if valid(nx,ny):
                    q.append([nx,ny])
        step += 1
    return step



# input
import re
lst = input()[1:-1]
lst = re.findall(r'\[(.*?)\]',lst)
for i in range(len(lst)):
    lst[i] = list(map(int,lst[i].split(',')))
sea = []
for x in range(len(lst)):
    for y in range(len(lst[0])):
        if lst[x][y] == 0:
            sea.append([x,y])
if len(sea) == len(lst[0]) * len(lst):
    print(-1)
else:
    max_len = -1
    while sea:
        notVisited = [[True for _ in range(len(lst[0]))] for _ in range(len(lst))]
        begin = sea.pop(0)
        max_len = max(max_len,bfs(begin[0],begin[1]))
    print(max_len)