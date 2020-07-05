from _collections import deque
s, temp_s = "", ""
while not temp_s.endswith(']'):
    temp_s = input()
    s += temp_s
grid = eval(s)
k = eval(input())

def sol():
    if len(grid) == 1 and len(grid[0]) == 1:
        return 0

    queue = deque([(0, 0, k, 0)])
    visited = set([(0, 0, k)])
    while queue:
        row, col, eliminate, steps = queue.popleft()
        for new_row, new_col in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] == 1 and eliminate > 0:
                    if (new_row, new_col, eliminate - 1) not in visited:
                        visited.add((new_row, new_col, eliminate - 1))
                        queue.append((new_row, new_col, eliminate - 1, steps + 1))
                if grid[new_row][new_col] == 0 and (new_row, new_col, eliminate) not in visited:
                    if new_row == len(grid) - 1 and new_col == len(grid[0]) - 1:
                        return steps + 1
                    visited.add((new_row, new_col, eliminate))
                    queue.append((new_row, new_col, eliminate, steps + 1))
    return -1
print(sol())