def f(s):
    m = len(s)
    n = len(s[0])
    matrix_set = set()
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for p in range(0, m - i + 1):
                for q in range(0, n - j + 1):
                    value = ''
                    for x in range(i):
                        for y in range(j):
                            value += s[p + x][q + y]
                    matrix_set.add((i, j, value))
    return len(matrix_set)


line = input().strip()
m = int(line.split()[0])
n = int(line.split()[1])
t = []
for i in range(m):
    t.append(list(input().strip()))

print(f(t),end='')

