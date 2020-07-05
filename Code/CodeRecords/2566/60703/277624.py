import sys
def Game(matrix:list):
    m = len(matrix)
    n = len(matrix[0])
    cache =[ [sys.maxsize for x in range(n)] for x in range(m)]
    # cache[0][0] = max(1-matrix[0][0],1)
    cache[m-1][n-1] = max(1-matrix[m-1][n-1],1)
    visited =  [[0 for x in range(n)] for y in range(m)]
    #visited[m-1][n-1]  = 1
    visited[0][0] = 1

    for k in range(m-2,-1,-1):
        cache[k][n-1] = max(1,cache[k+1][n-1]-matrix[k][n-1])
    for k in range(n-2,-1,-1):
        cache[m-1][k] = max(1,cache[m-1][k+1] - matrix[m-1][k])

    for i in range(m-2,-1,-1):
        for j in range(n-2,-1,-1):
            temp = min(cache[i+1][j],cache[i][j+1])
            cache[i][j] = max(1,temp-matrix[i][j])
    return cache[0][0]



matrix = []
N = int(input())
for i in range(N):
    matrix.append([int(x) for x in input().split(",")])
res = Game(matrix)
print(res)