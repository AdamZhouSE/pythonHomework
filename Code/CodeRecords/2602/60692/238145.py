list1 = input()[1:-1].split(",")
list2 = input()[1:-1].split(",")
list3 = [[0] * (len(list2) + 1) for i in range(len(list1) + 1)]
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            list3[i + 1][j + 1] = list3[i][j] + 1
max_num = max(max(x) for x in list3)
print(max_num)