nums = input().split(',')
target = int(input())
isFind = False
lst = []
n = len(nums)
i = 0
j = n - 1
while (i < j):
    if int(nums[i]) + int(nums[j]) == target:
        lst.append(i + 1)
        lst.append(j + 1)
        isFind = True
        break
    elif int(nums[i]) + int(nums[j]) > target:
        j -= 1
    else:
        i += 1
if isFind:
    print(lst)
else:
    print('None')
