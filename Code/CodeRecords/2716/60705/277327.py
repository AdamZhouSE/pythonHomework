line = input()
grid = []
while True:
    if line == "]":
        break
    if line == "[":
        continue
    grid.append(line)
    line = input()

print(grid)
