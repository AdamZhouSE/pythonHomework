def swimInWater(grid):
    N = len(grid)

    def possible(T):
        stack = [(0, 0)]
        seen = {(0, 0)}
        while stack:
            r, c = stack.pop()
            if r == c == N-1: return True
            for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if (0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen and grid[cr][cc] <= T):
                    stack.append((cr, cc))
                    seen.add((cr, cc))
        return False

    lo, hi = grid[0][0], N * N
    while lo < hi:
        mi = (lo + hi) / 2
        if not possible(mi):
            lo = mi + 1
        else:
            hi = mi
    return lo


a=eval(input())
print(int(swimInWater(a)))