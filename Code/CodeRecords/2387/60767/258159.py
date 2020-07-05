def ans(nums,operations,target):
    for op in operations:
        start = int(op[1])
        end = int(op[2])
        flag = op[0]
        if(int(flag)==0):
            nums = nums[:(start-1)] + sorted(nums[start-1:end]) + nums[end:]
        else:
            nums = nums[:(start - 1)] + sorted(nums[start - 1:end],reverse=True) + nums[end:]
    return nums[target-1]

temp = input().split()
numOfOperations = int(temp[1])
nums = []
temp = input().split()
for t in temp:
    nums.append(int(t))
operations = []
for i in range(numOfOperations):
    operations.append(input().split())
target = int(input())
print(ans(nums,operations,target))