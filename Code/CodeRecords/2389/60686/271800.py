nums = int(input())
list_all = []

for i in range(nums):
    len_input = int(input())
    list_temp = input().split(" ")
    for j in range(len_input):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
for i in range(nums):
    list_temp = list_all[i]
    for j in range(int(len(list_temp) / 2)):
        list_temp[2 * j], list_temp[2 * j + 1] = list_temp[2 * j + 1], list_temp[2 * j]
    for j in range(len(list_temp) - 1):
        print(list_temp[j],end=" ")
    print(list_temp[-1])