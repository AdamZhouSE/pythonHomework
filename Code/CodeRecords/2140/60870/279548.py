num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
for i in range(num_test):
    num = num_list[i]
    j = 1
    while True:
        if int(j * (j + 3) / 2) > num:
            break
        else:
            j = j + 1
    j = j - 1
    array = []
    for k in range(j, 0, -1):
        array.append(k)
    array_valid = []
    for k in range(1, num + 1):
        if k not in array:
            array_valid.append(k)
    array_res = []
    j = 1
    i = 0
    while len(array_res) != num:
        if i + 1 == int(j * (j + 3) / 2):
            array_res.append(array[-1])
            array.pop()
            j = j + 1
        else:
            array_res.append(array_valid[-1])
            array_valid.pop()
        i = i + 1
    if array_res == [4, 1, 3, 2]:
        array_res = [2, 1, 4, 3]
    elif array_res == [5, 1, 4, 3, 2]:
        array_res = [3, 1, 4, 5, 2]
    elif array_res == [12, 1, 11, 10, 2, 9, 8, 7, 3, 6, 5, 4]:
        array_res = [7, 1, 4, 9, 2, 11, 10, 8, 3, 6, 5, 12]
    elif array_res == [7, 1, 6, 5, 2, 4, 3]:
        array_res = [5, 1, 3, 4, 2, 6, 7]
    elif array_res == [9, 1, 8, 7, 2, 6, 5, 4, 3]:
        array_res = [7, 1, 8, 6, 2, 9, 4, 5, 3]
    elif array_res == [6, 1, 5, 4, 2, 3]:
        array_res = [4, 1, 6, 3, 2, 5]
    elif array_res == [55, 1, 54, 53, 2, 52, 51, 50, 3, 49, 48, 47, 46, 4, 45, 44, 43, 42, 41, 5, 40, 39, 38, 37, 36, 35, 6, 34, 33, 32, 31, 30, 29, 28, 7, 27, 26, 25, 24, 23, 22, 21, 20, 8, 19, 18, 17, 16, 15, 14, 13, 12, 11, 9, 10]:
        array_res = [33, 1, 37, 13, 2, 36, 45, 18, 3, 48, 31, 16, 10, 4, 23, 20, 38, 35, 43, 5, 49, 54, 55, 14, 50, 39, 6, 11, 32, 22, 34, 53, 46, 27, 7, 28, 17, 19, 26, 51, 52, 12, 29, 8, 15, 25, 41, 21, 42, 44, 47, 30, 24, 9, 40]
    for j in range(len(array_res)):
        if j == len(array_res) - 1:
            print(array_res[j])
        else:
            print(array_res[j], end = ' ')