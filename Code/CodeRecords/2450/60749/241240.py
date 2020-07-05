def search(nums,target):
    if len(nums)==0:
        return -1
    l=0
    r=len(nums)-1
    while l<=r:
        middle=(l+r)/2
        if nums[middle]==target:
            return middle
        elif nums[middle]>target:
            r=middle-1
        else:
            l=middle+1
    return -1

def search(nums,target):
    if len(nums)==0:
        return -1
    l=0
    r=len(nums)-1
    while l<=r:
        middle=(l+r)/2
        if nums[middle]==target:
            return middle
        elif nums[middle]>target:
            r=middle-1
        else:
            l=middle+1
    return -1

def searchrange(nums, target):
    if search(nums,target)==-1:
        return [-1,-1]

    index=search(nums,target)
    lower=index
    upper=index
    while upper<len(nums)-1:
        if nums[index+1]==target:
            upper+=1

        else:
            break
    while lower>0:
        if nums[index-1]==target:
            lower-=1
        else:
            break
    return [lower,upper]
nums=input()
target=int(input())
print(searchrange(nums,target))