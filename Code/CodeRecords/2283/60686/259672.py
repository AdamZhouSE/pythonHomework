def judge(list_temp_m):
    for y in range(list_temp_m.count(0)):
        print(0, end=" ")
    for y in range(list_temp_m.count(1)):
        print(1, end=" ")
    for y in range(list_temp_m.count(2)):
        print(2, end=" ")
    print()


num = int(input())
list_all = []
for i in range(num):
    # len_m, len_n = (int(x) for x in input().split(" "))
    n = int(input())
    list_input_m = input().split(" ")
    # list_input_n = input().split(" ")
    for j in range(len(list_input_m)):
        list_input_m[j] = int(list_input_m[j])
    list_input_m.sort()
    list_all.append(list_input_m)
    # for j in range(len(list_input_n)):
    #    list_input_n[j] = int(list_input_n[j])
    # list_input_n.sort()
    # list_all.append(list_input_n)
for x in range(num):
    judge(list_all[x])
