temp = input().split(',')
num = int(input())
array = []
for i in range(len(temp)):
    array.append(int(temp[i]))
array.sort()
for i in range(1, len(array)):
    if abs(array[i] - array[0] - 2 * num) > array[i] - array[0]:
        array[i] = array[i] + num
    else:
        array[i] = array[i] - num
array[0] = array[0] + num
print(max(array) - min(array))
