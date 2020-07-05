n = int(input())
mpa = []
for i in range(n):
    mpa.append(list(map(int, input().split(','))))
row_num = len(mpa)
col_num = len(mpa[0])
hp = [[1000 for i in range(col_num + 1)] for j in range(row_num + 1)]
hp[row_num][col_num - 1] = hp[row_num - 1][col_num] = 1
for i in range(row_num - 1, -1, -1):
    for j in range(col_num - 1, -1, -1):
        hp[i][j] = max(1, min(hp[i + 1][j], hp[i][j + 1]) - mpa[i][j])
print(hp[0][0])
