def maxDistance(grid):
    n = len(grid)
    steps = -1
    queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
    if len(queue) == 0 or len(queue) == n ** 2: return steps
    while len(queue) > 0:
        for _ in range(len(queue)): 
            x, y = queue.pop(0)
            for xi, yj in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if xi >= 0 and xi < n and yj >= 0 and yj < n and grid[xi][yj] == 0:
                    queue.append((xi, yj))
                    grid[xi][yj] = -1
        steps += 1
    return steps


str = input()[1:-2]
nums = str.split("],")
grip = []
for i in nums:
    tmp = [int(x) for x in i[1:].split(",")]
    grip.append(tmp)
print(maxDistance(grip))
