def union(array, i):
    if array[i][0] <= array[i - 1][1]:
        array[i - 1][1] = max(array[i - 1][1], array[i][1])
        array.pop(i)
    return array


number = int(input())
array = [[0 for _ in range(2)] for _ in range(number)]
for i in range(number):
    temp = input().split()
    array[i][0] = int(temp[0])
    array[i][1] = int(temp[1])
array.sort()
for i in range(len(array) - 1, 0, -1):
    array = union(array, i)
for i in range(len(array)):
    print(str(array[i][0]) + ' ' + str(array[i][1]))
