line = input()
grid = []
while True:
    if line == "]":
        break
    if line == "[":
        line = input()
        continue
    this_line = []
    count = 0
    for char in line:
        if char == '"':
            count += 1
            continue
        if count == 1:
            this_line.append(char)
    grid.append(this_line)

for item in grid:
    print(item)

