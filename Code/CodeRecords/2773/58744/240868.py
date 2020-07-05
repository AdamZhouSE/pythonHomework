import copy


end_sign = ']'
arr_str = ''
for m_line in iter(input, end_sign):
    arr_str += m_line

arr = list(eval(arr_str + end_sign))
line = len(arr)
col = len(arr[0])
directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
cache = list()
cache_line = [0] * col
for l in range(line):
    cache.append(copy.deepcopy(cache_line))

def longestIncreasingPath(matrix):
    ans = 0
    for i in range(line):
        for j in range(col):
            ans = max(ans, dfs(matrix, i, j))
    return ans

def dfs(matrix, i, j):
    if cache[i][j] != 0:
        return cache[i][j]

    for direct in directions:
        x, y = i + direct[0], j + direct[1]
        if x >= 0 and y >= 0 and x < line and y < col:
            if matrix[x][y] > matrix[i][j]:
                cache[i][j] = max(cache[i][j], dfs(matrix, x, y))
    cache[i][j] += 1
    return cache[i][j]
    
print(longestIncreasingPath(arr))
