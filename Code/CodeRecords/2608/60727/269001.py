def sub(string, char1, char2, length, res, array):
    if length == len(string):
        if array.count(char1 + res + char2) == 0:
            array.append(char1 + res + char2)
    else:
        sub(string, char1, char2, length + 1, res, array)
        sub(string, char1, char2, length + 1, res + string[length], array)


def search(strs, array):
    array1 = []
    array2 = []
    test = ["a", "e", "i", "o", "u"]

    n = len(strs)
    for i in range(0, n):
        if test.count(strs[i]) == 0:
            array2.append(i)
        else:
            array1.append(i)

    for i in range(0, len(array1)):
        for j in range(0, len(array2)):
            if array1[i] > array2[j]:
                continue
            else:
                sub(strs[array1[i] + 1:array2[j]], strs[array1[i]], strs[array2[j]], 0, "", array)


def sort(array):
    n = len(array)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                tem = array[i]
                array[i] = array[j]
                array[j] = tem
num = int(input())
while num > 0:
    num -= 1
    array = []
    search(input(), array)
    sort(array)
    if array:
        for i in range(0, len(array)):
            if i == len(array) - 1:
                print(array[i])
            else:
                print(array[i], end=" ")
    else:
        print("-1")