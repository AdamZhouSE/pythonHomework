line = input()
grid = []
while True:
    if line == "]":
        break
    grid.append(line)
    line = input()

print(grid)
