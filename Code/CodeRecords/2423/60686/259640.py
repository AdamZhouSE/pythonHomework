def judge(list_temp_m, list_temp_n):
    flag = True
    for y in range(len(list_temp_n)):
        if list_temp_m.count(list_temp_n[y]) == 0:
            flag = False
            break
        else:
            continue
    if flag:
        print("Yes")
    else:
        print("No")


num = int(input())
list_all = []
for i in range(num):
    len_m, len_n = (int(x) for x in input().split(" "))
    list_input_m = input().split(" ")
    list_input_n = input().split(" ")
    for j in range(len(list_input_m)):
        list_input_m[j] = int(list_input_m[j])
    list_input_m.sort()
    list_all.append(list_input_m)
    for j in range(len(list_input_n)):
        list_input_n[j] = int(list_input_n[j])
    list_input_n.sort()
    list_all.append(list_input_n)
for x in range(num):
    judge(list_all[x * 2], list_all[x * 2 + 1])
