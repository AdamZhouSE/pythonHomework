def findNum (src,nums):
    size=len(nums)
    lsmall=True
    rbig=True
    for i in range(src):
        if(nums[i]>nums[src]):
            lsmall=False
            break
    for j in range(src+1,size):
        if(nums[j]<nums[src]):
            rbig=False
            break
    return (lsmall and rbig)

testNum=int(input())
for i in range (testNum):
    size=int(input())
    rawInputs=input().split(' ')
    items =[]
    for rawInput in rawInputs:items.append(int(rawInput))
    ans=-1
    for s in range(1,size-1):
        if(findNum(s,items)):
            ans=items[s]
            break
    print(str(ans))