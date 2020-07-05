nums = int(input())
list_all = []
for i in range(nums):
    str_input = input()
    list_all.append(str_input)
for i in range(nums):
    str_input = list_all[i]
    list_num = []
    for m in range(len(str_input)):
        if '0' <= str_input[m] <= '9':
            list_num.append(int(str_input[m]))
        elif str_input[m] == '*':
            list_num[-2] = list_num[-1] * list_num[-2]
            list_num.pop(-1)
        elif str_input[m] == '+':
            list_num[-2] = list_num[-1] + list_num[-2]
            list_num.pop(-1)
        elif str_input[m] == '-':
            list_num[-2] = list_num[-2] - list_num[-1]
            list_num.pop(-1)
        elif str_input[m] == '/':
            list_num[-2] = list_num[-2] / list_num[-1]
            list_num.pop(-1)
    print(list_num[0])
