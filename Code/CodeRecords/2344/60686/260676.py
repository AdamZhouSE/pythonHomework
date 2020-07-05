def judge(list_temp, res):
    for a in range(res):
        list_temp.append(list_temp[0])
        list_temp.pop(0)
    for a in range(len(list_temp)):
        print(list_temp[a], end=" ")
    print()


num = int(input())
list_all = []
list_num = []
for i in range(num):
    n = int(input())
    list_input = input().split(" ")
    for j in range(n):
        list_input[j] = int(list_input[j])
    list_all.append(list_input)
    m = int(input())
for x in range(num):
    judge(list_all[x], m)
