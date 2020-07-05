def judge(list_temp):
    maximum = list_temp[0] * list_temp[1] * list_temp[2]
    for y in range(len(list_temp) - 2):
        for k in range(y + 1, len(list_temp) - 1):
            for l in range(k + 1, len(list_temp)):
                if list_temp[y] * list_temp[k] * list_temp[l] > maximum:
                     maximum = list_temp[y] * list_temp[k] * list_temp[l]
                else:
                    continue
    print(maximum)


num = int(input())
list_all = []
for i in range(num):
    nums = int(input())
    list_input = input().split(" ")
    for j in range(len(list_input)):
        list_input[j] = int(list_input[j])
    list_all.append(list_input)
for x in range(len(list_all)):
    judge(list_all[x])
