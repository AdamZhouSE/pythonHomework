def s8():
    array = list(eval(input()))
    first = 0
    last = len(array) - 1

    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            first = i-1
            break
    for i in range(len(array)-1, 1, -1):
        if array[i] < array[i-1]:
            last = i
            break
    print(last - first + 1)


s8()