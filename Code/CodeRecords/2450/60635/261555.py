nums=eval(input())
target=int(input())
ans=[]
def searchfirst(tar,left,right):
    while left<right:
        mid = (left + right) // 2
        if nums[mid]>=tar:
            right=mid
        else:
            left=mid+1
    return left if nums[left]==tar else -1
def searchlast(tar,left,right):
    while left<right:
        mid = (left + right) // 2
        if nums[mid]>tar:
            right=mid
        else:
            left=mid+1
    return left-1 if nums[left-1]==tar else -1
ans.append(searchfirst(target,0,len(nums)-1))
ans.append(searchlast(target,0,len(nums)-1))
print(ans)