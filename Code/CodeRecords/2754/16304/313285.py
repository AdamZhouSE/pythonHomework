import json

class Solution:
    def maxDistance(self, grid):
        
        n, m = len(grid), len(grid[0])
        
        dist = [[float('inf') for _ in range(m)] for _ in range(n)]
       
        visited = [[False for _ in range(m)] for _ in range(n)]
       
        q = []
        
        cnt = 0
        ans = 0
        tot = n * m
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    dist[i][j] = 0
                    visited[i][j] = True
                    q.append((i, j))
                    cnt += 1
       
        if cnt == tot or cnt == 0:
            return -1
        while q:
            x, y = q.pop(0) 
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                
                if 0 <= i < n and 0 <= j < m and not visited[i][j]:
                    dist[i][j] = min(dist[i][j], dist[x][y] + 1) 
                    ans = max(ans, dist[i][j]) 
                    visited[i][j] = True
                    q.append((i, j)) 
        return ans

def stringToInt2dArray(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            grid = stringToInt2dArray(line)
            
            ret = Solution().maxDistance(grid)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
