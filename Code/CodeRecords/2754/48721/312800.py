class Solution:
    def maxDistance(self, grid):
        m, n = len(grid), len(grid[0])
        result = []
        for i in range(m):
            for w in range(n):
                if grid[i][w] == 1:
                    result.append((i,w))
                else:
                    grid[i][w] = 0      
        if len(result) == 0 or len(result) == m * n:
            return -1
        count = 0
        while result:
            count += 1  
            for i in range(len(result)):
                x, y = result.pop(0)
                if x + 1 < m and grid[x+1][y] == 0:
                    result.append((x+1, y))
                    grid[x+1][y] = -1
                if x - 1 >= 0 and grid[x-1][y] == 0:
                    result.append((x-1, y))
                    grid[x-1][y] = -1
                if y + 1 < n and grid[x][y+1] == 0:
                    result.append((x, y+1))
                    grid[x][y+1] = -1
                if y - 1 >= 0 and grid[x][y-1] == 0:
                    result.append((x, y-1))
                    grid[x][y-1] = -1
        return count - 1


a=eval(input())
b=Solution()
ans=b.maxDistance(a)
print(ans)