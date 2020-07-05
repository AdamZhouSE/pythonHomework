def func21():
    arr1 = list(map(int, input()[1:-1].split(",")))
    arr2 = list(map(int, input()[1:-1].split(",")))
    bucket = []
    for i in range(1001):
        bucket.append(0)
    for i in range(len(arr1)):
        bucket[arr1[i]] += 1
    index = 0
    for i in range(len(arr2)):
        while bucket[arr2[i]] > 0:
            bucket[arr2[i]] -= 1
            arr1[index] = arr2[i]
            index += 1
    for i in range(len(bucket)):
        while bucket[i] > 0:
            bucket[i] -= 1
            arr1[index] = i
            index += 1
    print(arr1)
    return
func21()