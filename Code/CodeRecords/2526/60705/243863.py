line1 = input()[1:-1].split(",")
line2 = input()[1:-1].split(",")
tree = []
for i in range(0, len(line1)):
    if line1[i].isdigit():
        tree.append(int(line1[i]))

for i in range(0, len(line2)):
    if line2[i].isdigit():
        tree.append(int(line2[i]))

tree.sort()
print(tree)
