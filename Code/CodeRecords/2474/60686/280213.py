nums = int(input())
list_all = []
for i in range(nums):
    str_input = input()
    list_all.append(str_input)
for i in range(nums):
    str_input = list_all[i]
    count_left = 0
    count_right = 0
    length = 0
    max_length = 0
    for j in range(len(str_input)):
        if str_input[j] == '(':
            count_left += 1
        if str_input[j] == ')':
            if count_left != 0:
                length += 2
                if length > max_length:
                    max_length = length
                count_left -= 1
            else:
                length = 0
    print(max_length)