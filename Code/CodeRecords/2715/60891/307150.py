stones = eval(input())
rows_len = len(stones)
cols_len = len(stones[0])
rows = []
for i in range(rows_len):
    rows.append(0)
cols = []
for i in range(cols_len):
    cols.append(0)
for i in range(rows_len):
    for j in range(cols_len):
        if stones[i][j] == 1:
            rows[i] = 1
            cols[j] = 1
rows_cnt = rows.count(1)
cols_cnt = cols.count(1)
print(max(rows_cnt, cols_cnt))