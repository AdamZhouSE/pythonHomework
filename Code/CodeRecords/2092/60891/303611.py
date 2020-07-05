def np_not_end(np):
    np_len = len(np)
    for i in range(np_len):
        if np[i][i] != 0:
            return False
    return True


n = int(input())
t = [(int(i)) for i in input().split()]
tell_who_l = []
for i in range(n):
    tell_who_l.append([])
for i in range(n):
    tell_who_l[i].append(i + 1)
    tell_who_l[i].append(t[i])
np = []
for i in range(n):
    np.append([])
for i in range(n):
    for j in range(n):
        np[i].append(0)
for i in tell_who_l:
    np[i[0] - 1][i[1] - 1] = 1
while np_not_end(np):
    temp_l = []
    for i in range(n):
        for j in range(n):
            if np[i][j] != 0:
                temp_l.append([i, j, np[i][j]])
    for i in range(len(temp_l) - 1):
        for j in range(1, len(temp_l)):
            if temp_l[i][1] == temp_l[j][0]:
                np[temp_l[i][0]][temp_l[j][1]] = temp_l[i][2] + temp_l[j][2]
res_l = []
for i in range(n):
    if np[i][i] != 0:
        res_l.append(np[i][i])
print(min(res_l))
