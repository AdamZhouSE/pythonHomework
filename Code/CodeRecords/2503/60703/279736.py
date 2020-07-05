N = int(input())
matrix = [[0 for x in range(N)] for y in range(N)]
#邻接矩阵
edge = []
for i in range(N-1):
    r,c = [int(x)-1 for x in input().split(" ")]
    matrix[r][c] = 1
    matrix[c][r] = 1
    edge.append([r,c])
res = []


def dfs(node:int,road:list):
    flag = False
    for i in range(len(matrix[node])):
        if i not in road and matrix[node][i]==1:
            flag = True
            break
    if flag==False:
        res.append(len(road)-1)
        return
    else:
        for j in range(N):
            if j not in road and matrix[node][j]==1:
                road.append(j)
                dfs(j,road.copy())
                road = road[:-1]



for i in range(N):
    road = [i]
    dfs(i,road)
#print(max(res))

print(max(res))