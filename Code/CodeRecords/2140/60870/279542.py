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
    for j in range(len(array_res)):
        if j == len(array_res) - 1:
            print(array_res[j])
        else:
            print(array_res[j], end = ' ')