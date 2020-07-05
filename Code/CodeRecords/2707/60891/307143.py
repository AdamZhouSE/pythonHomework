row = eval(input())
tn = len(row)
cnt = 0
for i in range(0, tn, 2):
    if abs(row[i] - row[i + 1]) != 1 and min(row[i], row[i + 1]) % 2 != 0:
        cnt += 1
        # 保留row[i]
        if row[i] % 2 == 1:
            t = row.index(row[i] - 1)
        else:
            t = row.index(row[i] + 1)
        tmp = row[i]
        row[i] = row[t]
        row[t] = tmp
print(cnt)
