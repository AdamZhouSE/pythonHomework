arr = eval(input())


def heap(l):
    for i in range(l, -1, -1):
        sort(i, l)


def sort(j, l):
    if 2 * j + 1 <= l:
        if 2 * j + 2 > l:
            if arr[j] < arr[2 * j + 1]:
                arr[j], arr[2 * j + 1] = arr[2 * j + 1], arr[j]
        else:
            if arr[2 * j + 1] >= arr[2 * j + 2]:
                if arr[2 * j + 1] > arr[j]:
                    arr[j], arr[2 * j + 1] = arr[2 * j + 1], arr[j]
            else:
                if arr[2 * j + 2] > arr[j]:
                    arr[j], arr[2 * j + 2] = arr[2 * j + 2], arr[j]


for i in range(len(arr) - 1, -1, -1):
    heap(i)
    arr[0], arr[i] = arr[i], arr[0]
print(arr)