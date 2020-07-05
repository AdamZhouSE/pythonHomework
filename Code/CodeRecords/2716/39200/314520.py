root = {}
def find(i):
    if i not in root:
        root[i] = i
    if root[i] != i:
        root[i] = find(root[i])
    return root[i]


def union(x, y):
    root[find(x)] = find(y)
    return


# \0/
# 3*1
# /2\
input()
tgrid = []
string = input()
while string != "]":
    tgrid.append(string[string.index('"') + 1:len(string) - 1 - string[::-1].index('"')])
    string = input()
grid = []
for line in tgrid:
    newline = []
    x = 0
    while x < len(line):
        if line[x] == "\\":
            newline.append("\\")
            x += 2
        else:
            newline.append(line[x])
            x += 1
    grid.append(newline)
res = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if i:
            union((i, j, 0), (i - 1, j, 2))
        if j:
            union((i, j, 3), (i, j - 1, 1))
        if grid[i][j] != "/":
            union((i, j, 0), (i, j, 1))
            union((i, j, 2), (i, j, 3))
        if grid[i][j] != "\\":
            union((i, j, 0), (i, j, 3))
            union((i, j, 1), (i, j, 2))
print(len(set(map(find, root))))
