def ShiftZero(nums):
    ans = []
    size=len(nums)
    for num in nums:
        if (num != 0): ans.append(num)
    tmp = len(ans)
    for j in range(size -tmp):
        ans.append(0)
    return ans

testNum=int(input())
for i in range (testNum):
    size=int(input())
    rawInputs=input().split(' ')
    items=[]
    for rawInput in rawInputs:items.append(int(rawInput))
    for j in range(size-1):
        if(items[j]!=0 and items[j]==items[j+1]):
            items[j]=2*items[j]
            items[j+1]=0
    res=ShiftZero(items)
    print(' '.join(str(s)for s in res))