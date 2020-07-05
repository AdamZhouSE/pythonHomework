n=int(input())
nums=input().split(' ')
nums=[int(x) for x in nums]
if n<=2:
    print('NO')
    exit()
nums.sort()
mid=len(nums)/2
if mid%1!=0:
    mid=int(mid)
    if nums[mid-1]+nums[mid]>nums[mid+1]:
        print('YES')
    else:
        print('NO')
else:
    mid=int(mid)
    if nums[mid-1]+nums[mid]>nums[mid+1] or nums[mid+1]+nums[mid]>nums[mid+2]:
        print('YES')
    else:
        print('NO')