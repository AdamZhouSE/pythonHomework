board = list(input().split(","))
result = True
o_count, x_count = 0, 0
for line in board:
    if line == "XXX" or "OOO":
        result = False
    for j in line:
        if j == 'X':
            x_count += 1
        elif j == 'O':
            o_count += 1
print(result)