nums = int(input())
list_all = []
for i in range(nums):
    length = int(input())
    list_temp = input().split(" ")
    for j in range(length):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
for i in range(nums):
    list_temp = list_all[i]
    flag = False
    for j in range(1, len(list_temp) - 1):
        if max(list_temp[0:j]) <= list_temp[j] <= min(list_temp[j + 1:len(list_temp)]):
            if not flag:
                print(list_temp[j])
                flag = True
            continue
    if not flag:
        print(-1)