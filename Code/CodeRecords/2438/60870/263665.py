array_str = input()
array_str = array_str[1:-1]
array_list = array_str.split(',')
array_list.sort()
print('[', end = '')
for i in range(len(array_list)):
    if i == len(array_list) - 1:
        print(array_list[i], end = '')
    else:
        print(array_list[i] + ',', end = ' ')
print(']')