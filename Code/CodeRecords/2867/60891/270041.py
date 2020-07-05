a = []
i_index = 0
j_index = 0
for i in range(5):
    a.append([int(i) for i in input().split()])
for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            i_index = i
            j_index = j
            break
    else:
        continue
    break

res = abs(2 - i_index) + abs(2 - j_index)
print(res)
