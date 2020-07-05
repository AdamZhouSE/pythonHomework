line = input()
grid = []
while True:
    if line == "]":
        break
    if line == "[":
        line = input()
        continue
    grid.append(line)
    line = input()

for item in grid:
    print(item)
    
