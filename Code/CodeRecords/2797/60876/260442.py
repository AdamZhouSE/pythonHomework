n=int(input())
nums=list(map(int,input().split(" ")))
length=len(nums)
if length==1 and nums[0]!=0 and nums[0]!=15:
    print(-1)
else:
    if nums[length-1]==0:
        print("UP")
    elif nums[length-1]==15:
        print("DOWN")
    else:
        if nums[length-1]>nums[length-2]:
            print("UP")
        else:
            print("DOWN")