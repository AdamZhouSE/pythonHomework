def judge(list_temp):
    count = 0
    for a in range(len(list_temp)):
        for b in range(i, len(list_temp) - 1):
            if list_temp[b] > list_temp[b + 1]:
                count += 1
                list_temp[b], list_temp[b + 1] = list_temp[b + 1], list_temp[b]
    print(count)


num = int(input())
list_all = []
list_num = []
for i in range(num):
    n = int(input())
    list_input = input().split(" ")
    for j in range(n):
        list_input[j] = int(list_input[j])
    list_all.append(list_input)
for x in range(num):
    judge(list_all[x])
