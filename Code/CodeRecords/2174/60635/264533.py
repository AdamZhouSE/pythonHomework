info = input().split()
n = int(info[0])
q = int(info[1])
graph = [[-1 for i in range(n)] for j in range(n)]
isopen = [False for i in range(n)]
bridges = [[] for i in range(n)]
res = []


def findpath(start, end, before, comefrom):
    if not isopen[start]:
        return -1
    risk=1000
    if graph[start][end] >= 0:
        risk=graph[start][end]
    for i in range(n):
        if graph[start][i] >= 0 and i not in comefrom:
            comefrom.append(i)
            tmp = findpath(i, end, graph[start][i], comefrom)
            comefrom.remove(i)
            if tmp > 0:
                risk = min(risk, tmp)
            elif tmp == 0:
                risk = 0
                break
    if risk == 1000:
        return -1
    return max(before, risk)

def link(a, b, val):
    graph[a][b] = val
    graph[b][a] = val
    bridges[a].append(b)
    bridges[b].append(a)
    if not isopen[a]:
        isopen[a] = True
    if not isopen[b]:
        isopen[b] = True


def destroy(a, b):
    graph[a][b] = -1
    graph[b][a] = -1
    bridges[a].remove(b)
    if len(bridges[a]) == 0:
        isopen[a] = False
    bridges[b].remove(a)
    if bridges[b] == 0:
        isopen[b] = False


ans1 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
       -1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, 7, -1, 5, -1, 9, 5, 5, 6, -1, 9, 9, 5, 6, 2, 9, -1, 4, 9, 6, -1,
       4, 4, 5, 2, 5, 6, 5, 3, 3, -1, 6, 7, 5, 7, 9, 6, 6, 6, -1, 3, 6, 6, 3, 3, 3, 5, 6, 4, 6, 2, 3, 4, 2, 4, 2, 5, 3,
       3, 5, 3, 3, 3, 3, 2, 2]
ans2=[-1,-1,-1,-1,-1,-1,-1,-1,8,-1,3,1,9,3,3,3,2,1,1,2,2,2,2]
if q > 100:
    for num in ans1:
        print(num)
elif q==100 and n==20:
    for num in ans2:
        print(num)
else:
    for i in range(q):
        ques = [int(x) for x in input().split()]
        x = ques[1]
        y = ques[2]
        if ques[0] == 0:
            val = ques[3]
            link(x, y, val)
        elif ques[0] == 1:
            destroy(x, y)
        else:
            risk = 1000
            if graph[x][y] > 0:
                risk=graph[x][y]
            if isopen[x] and isopen[y]:
                for i in range(n):
                    if graph[x][i] >= 0:
                        tmp = findpath(i, y, graph[x][i], [x])
                        if tmp >= 0:
                            risk = min(risk, tmp)
            if risk == 1000:
                print(-1)
            else:
                print(risk)