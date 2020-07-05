nums = []
for i in range(int(input())):nums.append([int(j) for j in input().split(',')])
out = 0
for i in range(len(nums)):
    out+=max(nums[i])
    out+=max([nums[j][i] for j in range(len(nums))])
    for j in range(len(nums[0])):
        if(nums[i][j]>0):out+=1
print(out)