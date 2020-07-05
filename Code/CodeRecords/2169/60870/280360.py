num_test = int(input())
str_list = []
for i in range(num_test):
    str_input = input()
    str_list.append(str_input)
for i in range(num_test):
    str_input = str_list[i]
    stack_num = []
    stack_operator = []
    for ch in str_input:
        if '9' >= ch >= '0':
            stack_num.append(int(ch))
        else:
            num_1 = stack_num.pop()
            num_2 = stack_num.pop()
            if ch == '+':
                num_temp = num_1 + num_2
                stack_num.append(num_temp)
            elif ch == '-':
                num_temp = num_2 - num_1
                stack_num.append(num_temp)
            elif ch == '*':
                num_temp = num_1 * num_2
                stack_num.append(num_temp)
            else:
                num_temp = int(num_2 / num_1)
                stack_num.append(num_temp)
    print(stack_num.pop())