def searchT(nums,target):
    start=0
    end=len(nums)-1
    if(nums[-1]<target):
        return -1
    elif(nums[0]>target):
        return -1
    while(start<=end):
        mid=int((start+end)/2)
        if(nums[mid]==target):
            return mid
        elif(nums[mid]>target):
            end=mid
        else:
            start=mid
    return -1
nums=list(map(int,input()[1:-1].split(",")))
target=int(input())
print(searchT(nums,target))