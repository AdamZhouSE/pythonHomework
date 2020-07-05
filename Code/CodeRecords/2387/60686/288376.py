length,nums = (int(x) for x in input().split(" "))
list_input = input().split(" ")
list_all = []
for i in range(length):
    list_input[i] = int(list_input[i])
for i in range(nums):
    list_temp = input().split(" ")
    for j in range(len(list_temp)):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
ques = int(input())
for i in range(nums):
    list_temp = list_all[i]
    if list_temp[0] == 0:
        list_order = list_input[list_temp[1] -1:list_temp[2]]
        list_order.sort()
        for j in range(list_temp[1] - 1,list_temp[2]):
            list_input[j] = list_order[j - list_temp[1] + 1]
    else:
        list_order = list_input[list_temp[1] - 1:list_temp[2]]
        list_order.sort()
        list_order = list_order[::-1]
        for j in range(list_temp[1] - 1, list_temp[2]):
            list_input[j] = list_order[j - list_temp[1] + 1]
print(list_input[ques - 1])