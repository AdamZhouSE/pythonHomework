from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        res = [[-1 for _ in range(m)] for __ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    res[i][j] = 0
        while q:
            c = q.popleft()
            for nb in ((c[0]-1, c[1]), (c[0]+1, c[1]), (c[0], c[1]-1), (c[0], c[1]+1)):
                if 0 <= nb[0] < n and 0 <= nb[1] < m and res[nb[0]][nb[1]] < 0:
                    res[nb[0]][nb[1]] = res[c[0]][c[1]] + 1
                    q.append(nb)
        return res
    
