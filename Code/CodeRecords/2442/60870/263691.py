array_str = input()
array_str = array_str[1:-1]
array_list = array_str.split(',')
for i in range(len(array_list)):
    array_list[i] = int(array_list[i])
array_list.sort()
if len(array_list) == 1:
    print(0)
else:
    maxDiff = abs(array_list[0] - array_list[1])
    for i in range(len(array_list) - 1):
        if abs(array_list[i] - array_list[i + 1]) > maxDiff:
            maxDiff = abs(array_list[i] - array_list[i + 1])
    print(maxDiff)