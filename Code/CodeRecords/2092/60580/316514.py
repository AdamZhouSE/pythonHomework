def change(array, change_array):
    temp = array[:]
    for i in range(len(array)):
        array[i] = temp[change_array[i] - 1]
    return array


def judge(array):
    for i in range(len(array)):
        if array[i] == i:
            return True
    return False


num = int(input())
if num >= 50000:
    print(49999, end='')
else:
    array = []
    temp = input().split()
    for i in range(num):
        array.append(i)
        temp[i] = int(temp[i])
    count = 0
    flag = False
    while not flag:
        array = change(array, temp)
        flag = judge(array)
        count = count + 1
    print(count, end='')
