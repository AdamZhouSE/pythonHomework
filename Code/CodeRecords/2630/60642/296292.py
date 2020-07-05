def suber(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(nums[i][j]>0): nums[i][j]-=1
    return nums

def findPath(nums):
    nums[0][0]=-1
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(nums[i][j]==-1):
                if(i<len(nums)-1 and nums[i+1][j]==0):
                    nums[i+1][j]=-1
                if(i>0 and nums[i-1][j]==0):
                    nums[i-1][j]=-1
                if(j<len(nums)-1 and nums[i][j+1]==0):
                    nums[i][j+1]=-1
                if(j>0 and nums[i][j-1]==0):
                    nums[i][j-1]=-1
    return nums[-1][-1]==-1

nums = eval(input())
for i in range(max(max(nums))):
    nums = suber(nums)
    if(findPath(nums)):
        print(i+1)
        break