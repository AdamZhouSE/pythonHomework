def searchRange(nums, target):
        def find_left(m,n):
            if m>n:return -1
            mid=(m+n)//2
            if (nums[mid]==target and mid==0) or (nums[mid]==target and nums[mid-1]!=target):return mid
            elif nums[mid]>target or (nums[mid]==target and nums[mid-1]==target):return find_left(m,mid-1)
            else:return find_left(mid+1,n)
        def find_right(m,n):
            if m>n:return -1
            mid=(m+n)//2
            if (nums[mid]==target and mid==len(nums)-1) or (nums[mid]==target and nums[mid+1]!=target):return mid
            elif nums[mid]<target or (nums[mid]==target and nums[mid+1]==target):return find_right(mid+1,n)
            else:return find_right(m,mid-1)
        if len(nums)==0:return [-1,-1]
        if target >=nums[0] and target <=nums[-1]:
            left = find_left(0,len(nums)-1)
            if left==-1:return [-1,-1]
            elif left==len(nums)-1 or nums[left+1]!=target:return [left,left]
            else:return [left,find_right(left+1,len(nums)-1)]
        else:return [-1,-1]
nums=list(map(int,input().split(',')))
t=int(input())
print(searchRange(nums,t))
