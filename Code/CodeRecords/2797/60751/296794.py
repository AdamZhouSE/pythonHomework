num=int(input())
nums=list(map(int,input().split(" ")))
if len(nums)==1:
    if nums[0]!=0:
        print(-1)
    else:
        print("UP")
else:
    if nums[-1]>nums[-2] :
        if nums[-1]==15:
            print("DOWN")
        else:
            print("UP")
    else:
        if nums[-1]==0:
            print("UP")
        else:
            print("DOWN")
