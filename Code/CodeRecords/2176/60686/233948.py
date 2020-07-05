nums = input()
length = len(nums)
arr = []
arrs = []
for i in range(0, length):
    arr.append(i + 1)
    arrs.append(nums[i])
for j in range(1, length):
    tempnum = j
    while arrs[j] <= arrs[j - 1]:
        temp = arr[j - 1]
        arr[j - 1] = arr[j]
        arr[j] = temp
        temps = arrs[j - 1]
        arrs[j - 1] = arrs[j]
        arrs[j] = temps
        j -= 1
        if j == 0:
            break
    j = tempnum
for i in range(0, length - 1):
    print(arr[i],end=" ")
print(arr[length - 1])