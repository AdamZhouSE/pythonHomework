line1 = list(map(int, input()[1:-1].split(",")))
line2 = list(map(int, input()[1:-1].split(",")))
tree = line1 + line2
tree.sort()
print(tree)