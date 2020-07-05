#@grid 二维数组
def solve(grid):
    s = dict()

    def find(x):
        s.setdefault(x, x)
        if s[x] != x:
            s[x] = find(s[x])

        return s[x]

    def union(x, y):
        s[find(x)] = find(y)

    grid_len = len(grid)
    for i in range(grid_len):
        for j in range(grid_len):
            if i:
                union((i, j, 0), (i - 1, j, 2))
            if j:
                union((i, j, 3), (i, j - 1, 1))
            if grid[i][j] != '/':
                union((i, j, 0), (i, j, 1))
                union((i, j, 3), (i, j, 2))
            if grid[i][j] != '\\':
                union((i, j, 0), (i, j, 3))
                union((i, j, 2), (i, j, 1))

    return len(set(map(find, s)))

def change(str):
    re = []
    for s in str:
        re.append(s)
    return re

if __name__ == '__main__':
    str = input()
    re = []
    while True:
        str = input()
        if str == ']':
            break
        else:
            if(str[len(str)-1]==','):
                str = str[1:len(str)-2]
                re.append(change(str))
            else:
                str = str[1:len(str) - 1]
                re.append(change(str))
    #print(re)
    print(solve(re))