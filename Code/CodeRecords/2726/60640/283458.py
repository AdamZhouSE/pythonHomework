inp = eval(input().replace("null", "None"))
num = len(inp)
depth = 0
elements = 0
while elements < num:
    elements += 1 << depth
    depth += 1
print(depth-1)
