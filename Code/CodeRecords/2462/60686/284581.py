list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
left_flag = True
right_flag = False
index = 0
res = []
for i in range(len(list_input)):
    if i == len(list_input) - 1:
        if list_input[i] > list_input[i - 1]:
            print(i)
            exit(-1)
    elif i == 0:
        if list_input[i] > list_input[i + 1]:
            print(0)
            exit(0)
    else:
        if list_input[i - 1] < list_input[i] > list_input[i + 1]:
            print(i)
            exit(0)
