def getRoot(root, i):
    if root[i] == i:
        return i
    else:
        return getRoot(root, root[i])
    
s = input()
pairs = [[int(y) for y in x.split(",")] for x in input()[2:-2].split("],[")]
root = {i : i for i in range(len(s))}
for x, y in pairs:
    px, py = getRoot(root, x), getRoot(root, y)
    if px != py:
        root[px] = py
for x in range(len(s) - 1):
    for y in range(x + 1, len(s)):
        if getRoot(root, x) == getRoot(root, y) and ord(s[x]) > ord(s[y]):
            s = s[:x:] + s[y] + s[x + 1:y:] + s[x] + s[y + 1::]
print(s)
