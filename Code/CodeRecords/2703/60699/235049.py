inp = input()
length = len(inp)
list = []
i = 0
while i <= length - 1:
    temp = []
    while i <= length - 1:
        if inp[i].isdigit():
            temp.append(int(inp[i]))
        elif inp[i] == ']':
            break;
        i += 1
    i += 1
    if (len(temp) != 0):
        list.append(temp)
M=list
parent = [-1 for _ in range(len(M))]


def find(parent, i):
    if parent[i] == -1: return i
    return find(parent, parent[i])


def union(parent, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot != yroot:
        parent[xroot] = yroot


def union_find(Matrix):
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if Matrix[i][j] == 1 and i != j:
                union(parent, i, j)
    count = 0
    for i in range(len(parent)):
        if parent[i] == -1:
            count += 1
    return count


print(union_find(M))
