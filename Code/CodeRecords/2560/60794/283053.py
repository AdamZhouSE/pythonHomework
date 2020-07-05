num = int(input())
delete_num = []
e = []
for i in range(num):
    temp = input()
    delete_num.append(input().split(" "))
    e.append(int(input()))
for i in range(num):
    d = {}
    for j in range(len(delete_num[i])):
        if delete_num[i][j] not in d:
            d[delete_num[i][j]] = 1
        else:
            d[delete_num[i][j]] = d[delete_num[i][j]] + 1
    value = list(d.values())
    while e[i] != 0:
        if e[i] >= min(value):
            e[i] = e[i] - min(value)
            value.remove(min(value))
        else:
            e[i] = 0
    print(len(value))