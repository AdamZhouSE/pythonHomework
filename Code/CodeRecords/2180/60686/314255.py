str_1 = input()
str_2 = input()
Dict_1 = {}
Dict_2 = {}
for i in range(len(str_1)):
    for j in range(i, len(str_1)):
        if str_1[i:j + 1] in Dict_1:
            Dict_1[str_1[i:j + 1]] = Dict_1[str_1[i:j + 1]] + 1
        else:
            Dict_1[str_1[i:j + 1]] = 1
for i in range(len(str_2)):
    for j in range(i, len(str_2)):
        if str_2[i:j + 1] in Dict_2:
            Dict_2[str_2[i:j + 1]] = Dict_2[str_2[i:j + 1]] + 1
        else:
            Dict_2[str_2[i:j + 1]] = 1
res = 0
for k in Dict_1.keys():
    if k in Dict_2.keys():
        res = res + Dict_1[k] * Dict_2[k]
print(res, end = '')