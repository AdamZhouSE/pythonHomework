info = input().split()
info = [int(x) for x in info]
row = info[0]
column = info[1]
row_list = []
for i in range(row):
    element = input()
    row_ele = []
    for ch in element:
        row_ele.append(ch)
    row_list.append(row_ele)
column_list = []
for i in range(column):
    column_ele = []
    for j in range(row):
        column_ele.append(row_list[j][i])
    column_list.append(column_ele)
cnt = 0
# 对每种矩形类型进行遍历
for i in range(1, row + 1):
    for j in range(1, column + 1):
        dict_check = {}
        for p1 in range(0, column):
            column_start = p1
            temp_group = []
            if column_start + j > column:
                continue
            for p11 in range(column_start, column_start + j):
                for p2 in range(0, row):
                    temp = []
                    row_start = p2
                    if row_start + i > row:
                        continue
                    for p22 in range(row_start, row_start + i):
                        if p11 >= column:
                            continue
                        if p22 >= row:
                            continue
                        temp.append(row_list[p22][p11])
                    if p11 >= column:
                        continue
                    if p22 >= row:
                        continue
                    if p11 == column_start:
                        temp_group.append(temp)
                    else:
                        for ch in temp:
                            temp_group[p2].append(ch)
            for ch in temp_group:
                ch = str(ch)
                if ch not in dict_check.keys():
                    dict_check[ch] = 1
                else:
                    pass
        cnt = cnt + len(dict_check)
print(cnt)