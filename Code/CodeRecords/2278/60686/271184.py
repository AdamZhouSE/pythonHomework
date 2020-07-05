n = int(input())
list_all = []
for i in range(n):
    nums = int(input())
    list_temp = input().split()
    for j in range(nums):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
for i in range(n):
    list_temp = list_all[i]
    for j in range(len(list_temp) - 1):
        list_temp[j] = list_temp[j] ^ list_temp[j + 1]
    for j in range(len(list_temp) - 1):
        print(list_temp[j], end=" ")
    print(list_temp[-1])
