nums = int(input())
list_all = []
for i in range(nums):
    length = int(input())
    list_temp = input().split(" ")
    for j in range(length):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
for i in range(nums):
    count = 0
    list_temp = list_all[i]
    for j in range(len(list_temp) - 2):
        for k in range(j + 1, len(list_temp) - 1):
            for m in range(k + 1, len(list_temp)):
                if max(list_temp[j], list_temp[k], list_temp[m]) * 2 == list_temp[j] + list_temp[k] + list_temp[m]:
                    count += 1
    if count == 0:
        print(-1)
    else:
        print(count)
