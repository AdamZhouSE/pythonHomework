import sys

def reverser(nums,i,j):
    if(i<len(nums)-1):
        if(nums[i+1][j]==1):
            nums[i + 1][j]=-1
            reverser(nums,i+1,j)
    if(i>0):
        if (nums[i - 1][j] == 1):
            nums[i - 1][j] = -1
            reverser(nums, i - 1, j)
    if (j < len(nums[0]) - 1):
        if (nums[i][j+1] == 1):
            nums[i][j+1] = -1
            reverser(nums, i, j+1)
    if (j > 0):
        if (nums[i][j-1] == 1):
            nums[i][j-1] = -1
            reverser(nums, i, j-1)
    return nums

def finder(nums):
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if(nums[i][j]==1):
                return [i,j]
    return [-1,-1]

nums = []
for line in sys.stdin:
    temp = []
    if(line=='\n'):break
    for i in line.replace('\n',''):
        temp.append(int(i))
    nums.append(temp)
for i in range(100):
    temp = finder(nums)
    if(temp[0]==-1):
        break
    else:
        nums[temp[0]][temp[1]]=-1
        nums = reverser(nums,temp[0],temp[1])
print(i)