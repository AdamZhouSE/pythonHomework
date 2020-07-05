num_test = int(input())
str_list = []
for i in range(num_test):
    str_input = input()
    str_list.append(str_input)
for i in range(num_test):
    str_input = str_list[i]
    left = []
    array = []
    count = 0
    for ch in str_input:
        if ch == '(':
            count = count + 1
            left.append(count)
            array.append(count)
        elif ch == ')':
            array.append(left[-1])
            left.pop()
    for j in range(len(array)):
        if j == len(array) - 1:
            print(array[j])
        else:
            print(array[j], end = ' ')