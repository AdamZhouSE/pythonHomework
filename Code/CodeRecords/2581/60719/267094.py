ghosts = int(input())
al = []
for i in range(ghosts):
    g = input().split(",")
    g[0] = int(g[0])
    g[1] = int(g[1])
    al.append(g)
target = input().split(",")
target[0] = int(target[0])
target[1] = int(target[1])
m = abs(int(target[0])) + abs(int(target[1]))
for i in range(ghosts):
    al[i] = abs(al[i][0]-target[0])+abs(al[i][1]-target[1])
al.sort()
if al[0] <= m:
    print(False)
else:
    print(True)