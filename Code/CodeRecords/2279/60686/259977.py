def judge(list_temp_m, res):
    flag = False
    for y in range(len(list_temp_m)):
        temp = y
        temp_res = 0
        while res > temp_res:
            temp_res += list_temp_m[temp]
            temp += 1
            if temp == len(list_temp_m):
                break
        if res == temp_res:
            print(y + 1, end=" ")
            print(temp)
            flag = True
            break
        else:
            continue
    if not flag:
        print(-1)

num = int(input())
list_all = []
list_temp = []
for i in range(num):
    list_temp_n = input().split(" ")
    for j in range(2):
        list_temp_n[j] = int(list_temp_n[j])
    list_temp.append(list_temp_n)
    list_input_m = input().split(" ")
    # list_input_n = input().split(" ")
    for j in range(len(list_input_m)):
        list_input_m[j] = int(list_input_m[j])
    list_all.append(list_input_m)
    # for j in range(len(list_input_n)):
    #    list_input_n[j] = int(list_input_n[j])
    # list_input_n.sort()
    # list_all.append(list_input_n)
for x in range(num):
    judge(list_all[x], list_temp[x][1])
