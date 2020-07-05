def getRoot(root, i):
    if root[i] == i:
        return i
    else:
        return getRoot(root, root[i])
    
s = input()
pairs = [[int(y) for y in x.split(",")] for x in input()[2:-2].split("],[")]
print(pairs)
root = {i : i for i in range(len(s))}
for x in pairs:
    if getRoot(root, x[0]) == x[0]:
        root[x[0]] = x[1]
    elif getRoot(root, x[1]) == x[1]:
        root[x[1]] = x[0]
print(root)

