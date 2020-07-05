arr1 = input()
arr2 = input()
res = 0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        res = max(res, abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j))
print(res)