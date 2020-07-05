nums = eval(input())
for i in range(0,len(nums[0])-len(nums)+1):
    tem = []
    for j in range(0,len(nums)):
        tem.append(nums[j][i+j])
    tem.sort()
    for j in range(0,len(nums)):
        nums[j][i+j]=tem[j]
for i in range(len(nums[0])-len(nums)+1,len(nums[0])):
    tem = []
    for j in range(0,len(nums[0])-i-1):
        tem.append(nums[i][i+j])
    tem.sort()
    for j in range(0,len(nums[0])-i-1):
        nums[i][i+j]=tem[j]
for i in range(1,len(nums)):
    tem = []
    for j in range(0,len(nums)-i):
        tem.append(nums[i+j][j])
    tem.sort()
    for j in range(0,len(nums)-i):
        nums[i+j][j]=tem[j]
print(nums)