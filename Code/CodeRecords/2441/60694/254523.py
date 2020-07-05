def quickSort(arr, low, high):
    def partition(low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    if low < high:
        pi = partition(low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


arr = eval(input())
quickSort(arr, 0, len(arr)-1)
print(arr)
