def find_shortest_path(s, start, end):
    m = [(-1, 0)] * len(s)
    m[start] = (0, 1)
    t = find_adjacent(s, start)
    for k in t:
        m[k][0] = s[start][k]
    while True:
        a = choose_one(m)
        m[a][1] = 1
        if a == end:
            return m[a]
        else:
            b = find_adjacent(s, a)
            for k in b:
                if s[a][b] + m[a] < m[b]:
                    m[b][0] = s[a][b] + m[a]


def choose_one(m):
    min_value = 0
    min_index = 0
    for index in range(len(m)):
        if m[index][1] == 0 and m[index][0] > 0:
            min_value = m[index][0]
            min_index = index
    for index in range(len(m)):
        if m[index][1] == 0 and m[index][0] < min_value:
            min_value = m[index][0]
            min_index = index
    return min_index


def find_adjacent(s, i):
    t = []
    for j in range(len(s)):
        if s[i][j] != -1:
            t.append(j)

    return t


line1 = input()
dot = int(line1.split()[0])
edge = int(line1.split()[1])
start = int(line1.split()[2]) - 1
end = int(line1.split()[3]) - 1
print(dot)
s = [[-1] * dot for i in range(dot)]
for i in range(edge):
    line = input()
    x = int(line.strip().split()[0])-1
    y = int(line.strip().split()[1])-1
    value = int(line.split()[2])
    s[x][y] = value
    s[y][x] = value
print(find_shortest_path(s, start, end))
