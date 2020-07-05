def swap(nums,dest,src):
    tmp=nums[dest]
    nums[dest]=nums[src]
    nums[src]=tmp

testNum=int(input())
for i in range (testNum):
    size=int(input())
    rawInputs=input().split(' ')
    items=[]
    for rawInput in rawInputs:items.append(int(rawInput))
    items.sort()
    isEven=True
    for j in range(size-2):
        if(j%2!=0) :isEven=False
        else:isEven=True
        if(isEven):
            if(items[j]<items[j+1]):swap(items,j,j+1)
            if(items[j+1]>items[j+2]):swap(items,j+1,j+2)
        else:
            if (items[j] > items[j + 1]): swap(items, j, j + 1)
            if (items[j + 1] < items[j + 2]): swap(items, j + 1, j + 2)
    print(' '.join(str(s)for s in items))