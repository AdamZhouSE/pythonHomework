str_input = input()
str_input = str_input[1:-1]
array = str_input.split(',')
array = [int(x) for x in array]
odd_list = []
even_list = []
for ch in array:
    if ch % 2 == 0:
        even_list.append(ch)
    else:
        odd_list.append(ch)
array = []
for i in range(len(odd_list)):
    array.append(even_list[-1])
    even_list.pop()
    array.append(odd_list[-1])
    odd_list.pop()
for i in range(len(array)):
    if i == len(array) - 1:
        print(str(array[i]) + ']')
    elif i == 0:
        print('[' + str(array[i]) + ',', end = ' ')
    else:
        print(str(array[i]) + ',', end = ' ')