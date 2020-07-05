# 网格中的最短路径
import collections

def shortestPath(grid, k):
    m, n = len(grid), len(grid[0])
    if m == 1 and n == 1:
        return 0

    k = min(int(k), int(m + n - 3))
    visited = set([(0, 0, k)])
    q = collections.deque([(0, 0, k)])

    step = 0
    while len(q) > 0:
        step += 1
        cnt = len(q)
        for _ in range(cnt):
            x, y, rest = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 0 and (nx, ny, rest) not in visited:
                        if nx == m - 1 and ny == n - 1:
                            return step
                        q.append((nx, ny, rest))
                        visited.add((nx, ny, rest))
                    elif grid[nx][ny] == 1 and rest > 0 and (nx, ny, rest - 1) not in visited:
                        q.append((nx, ny, rest - 1))
                        visited.add((nx, ny, rest - 1))
    return -1

def getInput(input_str):
    nums_str1 = input_str.replace(' ', '')
    nums_str1 = nums_str1.replace('[', '')
    nums_str1 = nums_str1.replace(']', '')
    if nums_str1[-1] == ',':
        nums_str1 = nums_str1[0:len(nums_str1) - 1];

    nums = [int(n) for n in nums_str1.split(",")];
    return nums;

l = input()
matrix = []
while ']' in l:
    matrix.append(getInput(l))
    l = input()
k = int(l)
print(shortestPath(matrix, l))
