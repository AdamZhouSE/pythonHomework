def find_shortest_path(s, start, end):
    m=[]
    for i in range(len(s)):
        m.append([-1,0])
    m[start] = [0, 1]
    t = find_adjacent(s, start)
    for k in t:      
        m[k][0] = s[start][k]
    for l in range(len(s)-1):
        a = choose_one(m)
        
        m[a][1] = 1
        if a == end:
            return m[a][0]
        else:
            b = find_adjacent(s, a)
            
            for k in b:
                if s[a][k] + m[a][0] < m[k][0] or m[k][0]==-1:
                     
                    m[k][0] = s[a][k] + m[a][0]
            
    return 0


def choose_one(m):
    min_value = 0
    min_index = 0
    for index in range(len(m)):
        if m[index][1] == 0 and m[index][0] > 0:
            min_value = m[index][0]
            min_index = index
    for index in range(len(m)):
        if m[index][1] == 0 and m[index][0] < min_value and m[index][0]>0:
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
s = [[-1] * dot for i in range(dot)]
for i in range(edge):
    line = input()
    x = int(line.strip().split()[0])-1
    y = int(line.strip().split()[1])-1
    value = int(line.split()[2])
    s[x][y] = value
    s[y][x] = value
print(find_shortest_path(s, start, end))
