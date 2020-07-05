coordinates = []
co_len = int(input())
for i in range(co_len):
    coordinates.append([int(j) for j in input().split(",")])
is_line = True
ex_0 = coordinates[0]
ex_1 = coordinates[1]
# 大问题就是小数相等的问题，emm
if ex_0[0] == ex_1[0]:
    for i in coordinates:
        if i[0] != ex_0[0]:
            is_line = False
            break
else:
    slope = (ex_1[1] - ex_0[1]) / (ex_1[0] - ex_0[0])
    for i in range(co_len - 2):
        ex_i = coordinates[i + 2]
        slope_i = (ex_i[1] - ex_0[1]) / (ex_i[0] - ex_0[0])
        if slope_i != slope:
            is_line = False
            break
print(not is_line)
