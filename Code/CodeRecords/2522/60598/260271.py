arr1 = list(map(int, input()[1:-1].split(",")))
arr2 = list(map(int, input()[1:-1].split(",")))
left = 0
for i in range(len(arr2)):
    for j in range(left, len(arr1)):
        if arr1[j] == arr2[i]:
            temp = arr1[left]
            arr1[left] = arr1[j]
            arr1[j] = temp
            left += 1
arr1 = arr1[0:left]+sorted(arr1[left:])
print(arr1)
