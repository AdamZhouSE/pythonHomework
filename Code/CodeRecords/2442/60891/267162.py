inp = [int(i) for i in input()[1:-1].split(",")]
inp.sort()
max_diff = 0
for i in range(1, len(inp)):
    diff = inp[i] - inp[i - 1]
    if max_diff < diff:
        max_diff = diff

print(max_diff)
