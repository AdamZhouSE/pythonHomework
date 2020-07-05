nums = int(input())
list_num = []
for i in range(nums):
    str_input = input()
    list_num.append(str_input)
for i in range(nums):
    str_input = list_num[i]
    left_list = [0]
    res = []
    for j in range(len(str_input)):
        if str_input[j] == '(':
            if len(res) == 0:
                left_list.append(1)
                res.append(1)
            else:
                left_list.append(max(res) + 1)
                res.append(max(res) + 1)
        elif str_input[j] == ')':
            if left_list[-1] != 0:
                res.append(left_list[-1])
                left_list.pop(-1)
        else:
            continue
    for j in range(len(res)):
        print(res[j], end=" ")
    print()
