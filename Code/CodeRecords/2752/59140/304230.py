import collections


def bfs(forest, sr, sc, tr, tc):
    R, C = len(forest), len(forest[0])
    queue = collections.deque([(sr, sc, 0)])
    seen = {(sr, sc)}
    while queue:
        r, c, d = queue.popleft()
        if r == tr and c == tc:
            return d
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if (0 <= nr < R and 0 <= nc < C and
                    (nr, nc) not in seen and forest[nr][nc]):
                seen.add((nr, nc))
                queue.append((nr, nc, d+1))
    return -1

forest=[]
input()
temp=input()
forest.append([int(x) for x in temp[2:len(temp)-2].split(",")])
for i in range(1,len(forest[0])):
    temp=input()
    if i==len(forest[0])-1:forest.append([int(x) for x in temp[2:len(temp) - 1].split(",")])
    else:forest.append([int(x) for x in temp[2:len(temp) - 2].split(",")])
input()
trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
sr = sc = ans = 0
flag=True
for _, tr, tc in trees:
    d = bfs(forest, sr, sc, tr, tc)
    if d < 0:
        flag=False
        break
    ans += d
    sr, sc = tr, tc
if flag:print(ans)
else:print(-1)