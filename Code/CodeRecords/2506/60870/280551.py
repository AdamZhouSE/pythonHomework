str_input = input()
array = str_input.split(',')
array = [int(x) for x in array]
valid_list = []
for i in range(len(array)):
    temp_list = []
    temp = array[i]
    temp_list.append(array[i])
    for j in range(i + 1, len(array)):
        if array[j] > temp:
            temp_list.append(array[j])
            temp = array[j]
    valid_list.append(len(temp_list))
print(max(valid_list))