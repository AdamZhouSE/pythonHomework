def judge(list_temp, res):
    flag = False
    for y in range(len(list_temp) - 1):
        for k in range(y + 1, len(list_temp)):
            if list_temp[y] + list_temp[k] == res:
                print("Yes")
                flag = True
            else:
                continue
    if not flag:
        print("No")


num = int(input())
list_all = []
list_num = []
for i in range(num):
    n, m = (int(x) for x in input().split(" "))
    list_num.append(m)
    list_input = input().split(" ")
    for j in range(n):
        list_input[j] = int(list_input[j])
    list_all.append(list_input)
for x in range(num):
    judge(list_all[x], list_num[x])
