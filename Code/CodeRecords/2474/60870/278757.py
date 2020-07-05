num_test = int(input())
str_list = []
for i in range(num_test):
    str_input = input()
    str_list.append(str_input)
for i in range(num_test):
    str_input = str_list[i]
    left_stack = []
    valid_dict = {}
    for j in range(len(str_input) - 1):
        res = 0
        for k in range(j, len(str_input)):
            if len(left_stack) == 0 and str_input[k] == ')':
                break
            elif str_input[k] == '(':
                left_stack.append('(')
            elif str_input[k] == ')':
                left_stack.pop();
                res = res + 2
        valid_dict[res] = 1
    maxLen = max(valid_dict.keys())
    print(maxLen)