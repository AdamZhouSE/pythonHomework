import re;

def getInput():
    input()
    input_str = input();
    input_str = input_str.replace(",", '')
    matrixA = [];
    while(input_str != ']'):
        k = eval(input_str)
        matrixA.append(k);
        input_str = input();
        input_str = input_str.replace(",", '')

    return matrixA;


def regionsBySlashes(grid):
    N = len(grid)
    parent = [i for i in range(4 * N * N)]

    def find(parent, x):
        if parent[x] == x:
            return parent[x]
        return find(parent, parent[x])

    def union(parent, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)
        if x_root != y_root:
            parent[x_root] = y_root
    def union_find(grid):
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                top = 4 * (r * N + c)
                if val in ['/', ' ']:
                    union(parent, top + 0, top + 1)
                    union(parent, top + 2, top + 3)
                if val in ['\\', ' ']:
                    union(parent, top + 0, top + 2)
                    union(parent, top + 1, top + 3)

                if r + 1 < N:
                    union(parent, top + 3, top + (4 * N) + 0)
                if r - 1 >= 0:
                    union(parent, top + 0, top - (4 * N) + 3)
                if c + 1 < N:
                    union(parent, top + 2, top + 4 + 1)
                if c - 1 >= 0:
                    union(parent, top + 1, top - 4 + 2)

        return sum(parent[x] == x for x in range(4 * N * N))

    return union_find(grid)


matrix = getInput()
print(regionsBySlashes(matrix))