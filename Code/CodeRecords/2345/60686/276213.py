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
    lost = 0
    dual = 0
    for j in range(1, len(list_temp) + 1):
        if list_temp.count(j) == 0:
            lost = j
        if list_temp.count(j) == 2:
            dual = j
    print(dual, end=" ")
    print(lost)
