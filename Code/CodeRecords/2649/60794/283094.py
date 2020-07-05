num = int(input())
e = []
for i in range(num):
    e.append(input().split())
    for j in range(len(e[i])):
        e[i][j] = int(e[i][j])
for i in range(num):
    mm = bin(e[i][0])
    m = mm[2: len(mm)]
    for p in range(e[i][1], e[i][2]+1):
        j = len(m) - p
        if m[j] == '0':
            m = m[:j] + '1' + m[j+1:]
        else:
            m = m[:j] + '0' + m[j+1:]
    print(int(m, 2))