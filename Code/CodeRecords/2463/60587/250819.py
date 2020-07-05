nums = input().split(',')
target = int(input())
index1, index2 = 0, 0
for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if int(nums[i]) + int(nums[j]) == target:
            
            index1 = i + 1
            index2 = j + 1
            break
lst = []
lst.append(index1)
lst.append(index2)
print(lst)

