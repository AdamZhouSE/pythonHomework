num_test = int(input())
array_test = []
for i in range(num_test):
    size = int(input())
    array = input().split(' ')
    array_test.append(array)
for i in range(num_test):
    count = 0
    array = array_test[i]
    for index in range(len(array)):
        array[index] = int(array[index])
    for first in range(0, len(array) - 2):
        for second in range(first + 1, len(array) - 1):
            for third in range(second + 1, len(array)):
                if array[first] + array[second] > array[third] and array[first] + array[third] > array[second] and array[second] + array[third] > array[first]:
                    count = count + 1
    print(count)