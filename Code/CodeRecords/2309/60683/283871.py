N, M = [int(x) for x in input().split()]
mtx = [[0] * M for i in range(N)]
graph = [[] for i in range(N * 1000)]
ID = [[0] * M for i in range(N)]
ans = 0
numOf1 = 0
numOf3 = 0
for i in range(N):
    chars = list(input().strip())
    # print(chars)
    for j in range(M):
        if chars[j] == '*':
            continue
        elif chars[j] == '2':
            ans += 1
            continue
        elif chars[j] == '1':
            mtx[i][j] = 1
            numOf1 += 1
            ID[i][j] = numOf1
            if i != 0 and mtx[i][j] + mtx[i - 1][j] == 4:
                graph[ID[i][j]].append(ID[i - 1][j])
            if j != 0 and mtx[i][j] + mtx[i][j - 1] == 4:
                graph[ID[i][j]].append(ID[i][j - 1])

        elif chars[j] == '3':
            mtx[i][j] = 3
            numOf3 += 1
            ID[i][j] = numOf3
            if i != 0 and mtx[i][j] + mtx[i - 1][j] == 4:
                graph[ID[i - 1][j]].append(ID[i][j])
            if j != 0 and mtx[i][j] + mtx[i][j - 1] == 4:
                graph[ID[i][j - 1]].append(ID[i][j])
# print(numOf1)
# print(numOf3)
# print(ID)
# print(graph[1][1])
# print(mtx)
# 标识3（右边）匹配左边的哪个1
matches1 = [0] * (numOf3 + 1)
# 3是否已被访问过
visited = [False] * (numOf3 + 1)


def match(i) -> bool:
    j = 0
    while j < len(graph[i]):
        if not visited[graph[i][j]]:
            visited[graph[i][j]] = True
            if matches1[graph[i][j]] == 0 or match(matches1[graph[i][j]]):
                matches1[graph[i][j]] = i
                return True
        j += 1
    return False


def Hungarian() -> int:
    cnt = 0
    i = 1
    while i <= numOf1:
        if match(i):
            cnt += 1
        i += 1
    return cnt

print(ans + Hungarian())
