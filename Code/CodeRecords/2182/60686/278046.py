nums = int(input())
list_all = []
list_num = []
for i in range(nums):
    total_num, skip = (int(x) for x in input().split(" "))
    list_num.append(total_num)
    list_num.append(skip)
for i in range(nums):
    total_num = list_num[i * 2]
    skip = list_num[i * 2 + 1]
    list_play = [1] * total_num
    index = -1
    flag = True
    while list_play.count(1) > 1:
        if flag:
            count = 0
        index += 1
        if list_play[index % total_num] == 1:
            count += 1
            flag = False
        if count == skip:
            list_play[index % total_num] = 0
            flag = True
    print(list_play.index(1) + 1)
