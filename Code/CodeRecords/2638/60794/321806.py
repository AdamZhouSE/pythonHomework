def average(array, i, j):
    aver = 0
    for item in range(i - 1, j):
        aver = aver + array[item]
    aver = aver / (j - i + 1)
    return aver


def calculate_s(array, i, j):
    aver = average(array, i, j)
    total = 0
    for item in range(i - 1, j):
        total = total + (array[item] - aver) ** 2
    total = total / (j - i + 1)
    return total


number = input().split()
array = input().split()
for i in range(int(number[0])):
    array[i] = int(array[i])
for i in range(int(number[1])):
    temp = input().split()
    x = int(temp[1])
    y = int(temp[2])
    if temp[0] == '1':
        k = int(temp[3])
        for j in range(x - 1, y):
            array[j] = array[j] + k
    elif temp[0] == '2':
        result = average(array, x, y)
        print(format(result, '.4f'))
    else:
        result = calculate_s(array, x, y)
        print(format(result, '.4f'))
