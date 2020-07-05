info = int(input())
array = input().split(' ')
array = [int(x) for x in array]
res_list = []
for i in range(len(array)):
    temp_list = []
    for j in range(i, len(array)):
        temp_list.append(array[j])
    minValue = min(temp_list)
    minIndex = array.index(minValue) + 1
    tempIndex = temp_list.index(minValue)
    res_list.append(minIndex)
    reverse_list = []
    for j in range(0, tempIndex + 1):
        reverse_list.append(temp_list[j])
    reverse_list.reverse()
    for j in range(0, tempIndex + 1):
        array[i + j] = reverse_list[j]
for i in range(len(res_list)):
    if i == len(res_list) - 1:
        print(res_list[i], end = ' ')
    else:
        print(res_list[i], end = ' ')