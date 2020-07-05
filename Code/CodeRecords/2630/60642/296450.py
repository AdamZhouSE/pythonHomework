def suber(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(nums[i][j]>0): nums[i][j]-=1
            else:nums[i][j]=0
    return nums

def findPath(fnums):
    fnums[0][0]=-1
    fnums =searchPath(fnums, 0, 0)
    return fnums[-1][-1] == -1

def searchPath(searnums, i, j):
    if(searnums[-1][-1]==-1):
        return searnums
    if (i < len(searnums) - 1 and searnums[i + 1][j] == 0):
        searnums[i + 1][j] = -1
        searnums = searchPath(searnums, i + 1, j)
    if (i > 0 and searnums[i - 1][j] == 0):
        searnums[i - 1][j] = -1
        searnums = searchPath(searnums, i - 1, j)
    if (j < len(searnums) - 1 and searnums[i][j + 1] == 0):
        searnums[i][j + 1] = -1
        searnums = searchPath(searnums, i, j + 1)
    if (j > 0 and searnums[i][j - 1] == 0):
        searnums[i][j - 1] = -1
        searnums = searchPath(searnums, i, j - 1)
    #for i in nums:print(i)
    #print('')
    return searnums

nums = eval(input())
for i in range(max(max(nums))):
    nums = suber(nums)
    if(findPath(nums)):
        print(i+1)
        break