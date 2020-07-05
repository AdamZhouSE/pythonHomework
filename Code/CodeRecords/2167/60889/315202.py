def findlength(paths,now,target,hasReach):
    if now == target:
        return 0
    minLength = 0
    hasReach[now] = 1
    for i in range(len(paths)):
        if paths[now][i] != 0 and hasReach[i]==0:
            a = findlength(paths,i,target,hasReach.copy())
            if paths[now][i] > a:
                a = paths[now][i]
            if minLength == 0 or a < minLength:
                minLength = a
    return minLength


NML = input().strip(" ").split(" ")
n = int(NML[0])
m = int(NML[1])
l = int(NML[2])
colours = input().strip(" ").split(" ")
colours = list(map(int,colours))
paths = []
hasReach = []
for i in range(n):
    path = []
    for j in range(n):
        path.append(0)
    paths.append(path)
    hasReach.append(0)
for i in range(m):
    path = input().strip(" ").split(" ")
    path = list(map(int, path))
    s = path[0]
    e = path[1]
    length = path[2]
    paths[s-1][e-1] = length
    paths[e-1][s-1] = length
totalLength = 0
for i in range(n-1):
    for j in range(i+1,n):
        if abs(colours[i]-colours[j])>=l:
            totalLength = totalLength + findlength(paths,i,j,hasReach.copy())
print(totalLength)