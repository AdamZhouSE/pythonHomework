nums = int(input())
list_all = []
for i in range(nums):
    length = int(input())
    str_input = input().split(" ")
    for j in range(length):
        str_input[j] = int(str_input[j])
    list_all.append(str_input)
for i in range(nums):
    str_input = list_all[i]
    list_dual = []
    list_single = []
    for j in range(len(str_input)):
        if str_input[j] % 2 == 0:
            list_dual.append(str_input[j])
        else:
            list_single.append(str_input[j])
    for j in range(len(list_dual)):
        print(list_dual[j], end=" ")
    for j in range(len(list_single)):
        print(list_single[j], end=" ")
    print()
