# 可以发现是否能完成是根据时间的单调函数，因此可以用二分搜索来找到最少耗时。
# 即找到最小 T 使得从起点游到终点成为可能。
# 设最少耗时为 T，用深度优先搜索来检查是否有可能从起点游到终点。


def swimInWater(grid):
    N = len(grid)

    def DFS(T):
        stack = [(0, 0)]
        seen = {(0, 0)}
        while stack:
            r, c = stack.pop()
            if r == c == N - 1: return True
            for cr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= cr < N and 0 <= cc < N \
                        and (cr, cc) not in seen and grid[cr][cc] <= T:
                    stack.append((cr, cc))
                    seen.add((cr, cc))
        return False

    lo, hi = grid[0][0], N * N
    while lo < hi:
        mi = (lo + hi) // 2
        if not DFS(mi):
            lo = mi + 1
        else:
            hi = mi
    return lo


grid = eval(input())
print(swimInWater(grid))

