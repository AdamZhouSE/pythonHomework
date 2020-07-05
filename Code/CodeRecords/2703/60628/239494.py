def findCircleNum(M):
    visited = [0 for i in range(len(M))]
    count = 0
    for i in range(len(M)):
        if visited[i] == 0:
            count += 1
            dfs(M, i, visited, )
    return count

def dfs(M, i, visited):
    visited[i] = 1
    for j in range(len(M)):
        if M[i][j] == 1 and visited[j] == 0:
            dfs(M, j, visited)

inp = eval(input())
print(findCircleNum(inp))