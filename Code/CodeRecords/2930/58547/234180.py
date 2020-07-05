def local_min(arr, i):
    if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
        return True
    else:
        return False


def local_max(arr, i):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        return True
    else:
        return False


def func():
    n = int(input())
    arr = [int(x) for x in input().split(" ")]

    extremes = 0

    i = 1
    while i < n - 1:
        if local_max(arr, i) or local_min(arr, i):
            extremes += 1
        i += 1

    print(extremes)


func()
