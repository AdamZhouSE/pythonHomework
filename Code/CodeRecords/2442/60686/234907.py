arr = input().split(",")
arr[0] = arr[0][1]
arr[len(arr) - 1] = arr[len(arr) - 1][0:1]
for j in range(0, len(arr)):
    arr[j] = int(arr[j])
arr.sort()
maximum = 0
for i in range(1, len(arr)):
    if int(arr[i]) - int(arr[i - 1]) > maximum:
        maximum = int(arr[i]) - int(arr[i - 1])
print(maximum)
