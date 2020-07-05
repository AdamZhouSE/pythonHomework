num_test = int(input())
info_list = []
array_list = []
for i in range(num_test):
    info = int(input())
    array = input().split(' ')
    array = [int(x) for x in array]
    info_list.append(info)
    array_list.append(array)
for i in range(num_test):
    array = array_list[i]
    res = 0
    for j in range(1, len(array) - 1):
        if array[j] < array[j - 1] and array[j] < array[j + 1]:
            front = j - 1
            back = j + 1
            if front - 1 >= 0:
                while array[front - 1] > array[front]:
                    front = front - 1
                    if front - 1 < 0:
                        break
            if back + 1 < len(array):
                while array[back + 1] > array[back]:
                    back = back + 1
                    if back + 1 >= len(array):
                        break
            if array[front] > array[back]:
                base = array[back]
            else:
                base = array[front]
            for k in range(front + 1, back):
                res = res + base - array[k]
    print(res)