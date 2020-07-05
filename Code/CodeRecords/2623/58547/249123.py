def swap(arr, min_index, i):
    temp = arr[min_index]
    arr[min_index] = arr[i]
    arr[i] = temp


def func():
    arr = [int(x) for x in input().split(",")]
    k_th = int(input())

    #  use simple selection sort
    i = 0
    while i < k_th:
        j = i
        max_index = i
        flag = False
        while j < len(arr):
            if arr[j] > arr[max_index]:
                max_index = j
                flag = True
            j += 1
        if flag:
            swap(arr, max_index, i)
        i += 1

    print(arr[k_th - 1])


func()
