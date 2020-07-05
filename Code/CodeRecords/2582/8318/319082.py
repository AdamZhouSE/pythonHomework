arr1 = input().split(',')
arr2 = input().split(',')
res = 0
for i in range(len(arr1)):
            for j in range(len(arr2)):
                res = max(res, abs(int(arr1[i]) - int(arr1[j])) + abs(int(arr2[i]) - int(arr2[j])) + abs(i - j))
print(res)