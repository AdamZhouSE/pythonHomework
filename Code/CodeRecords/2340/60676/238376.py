def water_between_blocks(array):
    while array[0] < array[1]:
        array.remove(array[0])
        if len(array) == 1:
            return 0
    while array[-1] < array[-2]:
        array.remove(array[-1])
        if len(array) == 1:
            return 0
    return calculate(array, 0, len(array)-1)


def calculate(array, start, end):
    if end-start == 1:
        return 0
    for i in range(start+1, end):
        if array[i] > array[start] or array[i] > array[end]:
             return calculate(array, start, i) + calculate(array, i, end)
    sum = 0
    height = min(array[start], array[end])
    for i in range(start+1, end):
        sum += height - array[i]
    return sum


result = []
for i in range(int(input())):
    line1 = input()
    line2 = input().split(' ')
    for j in range(len(line2)):
        line2[j] = int(line2[j])
    result.append(water_between_blocks(line2))
for i in range(len(result)):
    print(result[i])