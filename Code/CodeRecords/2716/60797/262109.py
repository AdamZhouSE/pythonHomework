def regionsBySlashes(grid):
    n = len(grid)
    global fmap
    fmap = [-1] * n * n * 4
    for row in range(n):
        for column in range(n):
            temp = grid[row][column]
            ptr = (row * n + column) * 4
            if temp == ' ':
                union(ptr + 0, ptr + 1)
                union(ptr + 1, ptr + 2)
                union(ptr + 2, ptr + 3)
            if temp == '/':
                union(ptr + 0, ptr + 3)
                union(ptr + 1, ptr + 2)
            if temp == '\\':
                union(ptr + 0, ptr + 1)
                union(ptr + 2, ptr + 3)
            if row < n - 1:
                union(ptr + 2, ptr + 4 * n)
            if column < n - 1:
                union(ptr + 1, ptr + 4 + 3)

    return len({find(x) for x in range(4 * n * n)})

def find(x):
        if fmap[x] == -1:
            return x
        else:
            return find(fmap[x])

def union(x, y):
        px = find(x)
        py = find(y)
        if px != py:
            fmap[px] = py

if __name__ == "__main__":
    data = []
    isover = 0
    while(isover != 1):
        a = input().strip(' ,').strip('"')
        if a == "[":
            continue
        elif a == "]":
            isover = 1
            break
        else:
            '''
            n = len(a)
            i = 0
            while i < n:
                if a[i]== '\\' and a[i + 1]== '\\' and a[i + 2]== '\\' and a[i + 3]== '\\':
                    del a[i+1]
                    del a[i+2]
                    del a[i+3]
                i += 4
            data.append(a)
            '''
            c = []
            hasone = 0
            for b in a:
                if b == '\\':
                    if hasone == 0:
                        hasone = 1
                        continue
                    else:
                        c.append(b)
                        hasone = 0
                else:
                    c.append(b)
            data.append(c)
    re = regionsBySlashes(data)
    print(re)