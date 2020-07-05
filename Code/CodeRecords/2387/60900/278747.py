m = int(input().split(' ')[1])
nums = input().split(' ')
op =[]
for i in range(0,len(nums)):
    nums[i] = int(nums[i])
for i in range(0,m):
    op.append(input().split(' '))
    for j in range(0,3):
        op[i][j]=int(op[i][j])


k = int(input())
for i in range(0,m):
    new =[]
    if op[i][1]!=1:
        for j in range(0,op[i][1]-1):
            new.append(nums[j])
    temp = nums[(op[i][1] - 1):(op[i][2])]
    
    if op[i][0] == 1:
        temp.sort(reverse=True)
    else:
        temp.sort()
    
    for j in range(0,op[i][2]-op[i][1]+1):
        new.append(temp[j])

    if op[i][2]!= len(nums):
        for j in range(op[i][2],len(nums)):
            new.append(nums[j])

    nums =new
    
print(nums[k]-1)