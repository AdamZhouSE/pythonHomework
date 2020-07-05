class Solution:
    def shortestPath(self, grid, k) -> int:
        if not any(grid):
            return -1
        m, n = len(grid), len(grid[0])
        k = min(k, m+n-3)
        q = [(0, 0, k, 0)]
        visited = {(0, 0, k)}
        while q:
            x, y, rest, steps = q.pop(0)
            if x == m-1 and y == n-1:
                return steps
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < m and 0 <= ny < n:
                    nk = rest-grid[nx][ny]
                    if nk < 0 or (nx, ny, nk) in visited:
                        continue
                    q.append((nx, ny, nk, steps+1))
                    visited.add((nx, ny, nk))
        return -1


if __name__ == "__main__":
    inp = []
    try:
        while True:
            inp.append(input())
    except EOFError:
        s = Solution()
        lent = len(inp)
        K = int(inp[lent-1])
        arr = []
        for i in range(0, lent-1):
            save = []
            for j in range(0, len(inp[i])):
                if inp[i][j].isdigit():
                    save.append(int(inp[i][j]))
            arr.append(save)
        res = s.shortestPath(arr, K)
        print(res)
