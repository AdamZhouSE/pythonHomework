rawInput=input().split(',')
nums=[]
for item in rawInput:nums.append(int(item))
target=int(input())
length=len(nums)
if length==0:
    print('-1')
    exit()
left,right=0,length-1
while left<=right:
    mid=left+(right-left)//2
    if nums[mid]==target:
        print(mid)
        exit()
    if nums[mid]<nums[right]:
        if target<=nums[right] and nums[mid]<target:
            left=mid+1
        else:right=mid
    else:
        if target>=nums[left] and nums[mid] > target:
            right=mid
        else:left=mid+1
print('-1')