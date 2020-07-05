import math
nums = input()[1:-1].split(',')
k = int(input())
for i in range(0,len(nums)):
    nums[i] = int(nums[i])
store =[]
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        store.append(int(math.fabs(nums[j]-nums[i])))
store.sort()
print(store[k-1])