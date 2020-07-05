arr = input().split(",")
arr[0] = arr[0][1]
result = []
arr[len(arr) - 1] = arr[len(arr) - 1][0:len(arr[len(arr) - 1]) - 1]
if len(arr) == 1:
    print(0)
else:
    for j in range(0, len(arr)):
        result.append(int(arr[j]))
    result.sort()
    maximum = 0
    for i in range(1, len(arr)):
        if result[i] - result[i - 1] > maximum:
            maximum = result[i] - result[i - 1]
    print(maximum)
