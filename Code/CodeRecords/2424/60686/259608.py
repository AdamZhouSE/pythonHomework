def judge(list_temp):
    flag = False
    for y in range(len(list_temp)):
        if list_temp.count(list_temp[y]) % 2 != 0:
            print(list_temp[y])
            flag = True
            break
        else:
            continue
    if not flag:
        print(0)


num = int(input())
list_all = []
for i in range(num):
    nums = int(input())
    list_input = input().split(" ")
    for j in range(len(list_input)):
        list_input[j] = int(list_input[j])
    list_input.sort()
    list_all.append(list_input)
for x in range(len(list_all)):
    judge(list_all[x])
