arr1 = input().split(',')
arr2 = input().split(',')
max_num = 0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        count = abs(int(arr1[i]) - int(arr1[j])) + abs(int(arr2[i]) - int(arr2[j])) + abs(i - j)
        max_num = max(count, max_num)
print(max_num)