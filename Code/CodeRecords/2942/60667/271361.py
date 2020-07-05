n = int(input())
nums = input().split()

index = 0
result = []
while len(nums) != 0:
    maximum = 0
    index = 0
    for i in range(n):
        if int(nums[i][0]) > maximum:
            maximum = int(nums[i][0])
            index = i
        if int(nums[i][0])==maximum:  
            if int(nums[i][:min(len(nums[index]),len(nums[i]))]) > int(nums[index][:min(len(nums[index]),len(nums[i]))]):
                maximum = int(nums[i][0])
                index = i
    result.append(nums[index])        
    nums.remove(nums[index])
    n = n - 1
print(''.join(result),end = '')    