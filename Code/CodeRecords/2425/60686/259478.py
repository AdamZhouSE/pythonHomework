def judge(list_temp, number):
    for y in range(len(list_temp)):
        if number > list_temp[y]:
            dis = number - list_temp[y]
            continue
        elif number == list_temp[y]:
            print(0)
            break
        else:
            if list_temp[y] - number > dis:
                print(list_temp[y - 1])
                break
            else:
                print(list_temp[y])
                break


num = int(input())
list_all = []
for i in range(num):
    nums, expect_num = (int(x) for x in input().split(" "))
    list_input = input().split(" ")
    for j in range(len(list_input)):
        list_input[j] = int(list_input[j])
    list_input.sort()
    list_all.append(list_input)
for x in range(len(list_all)):
    judge(list_all[x], expect_num)
