def isPostOrder(nums,start,end):
    if start>=end:
        return True
    rootval=nums[end]
    flag=False
    mid=end
    for i in range(start,end):
        if flag==False and nums[i]>rootval:
            mid=i
            flag=True
        elif flag==True and nums[i]<rootval:
            return False
    return isPostOrder(nums,start,mid-1)&isPostOrder(nums, mid, end-1)


n=int(input())
if n==0:
    print('true')
else:
    nums=list(map(int,input().split(' ')))
    if (isPostOrder(nums, 0, n-1)):
        print('true')
    else:
        print('false')