n=int(input())
nums=list(map(int,input().split(" ")))
def upanddown(nums):
    if len(nums)==1:
        if nums[0]==15:
            print("DOWN")
        elif nums[0]==0:
            print("UP")
        else:
            print("-1")
    else:
        if nums[-1]==0:
            print("UP")
        elif nums[-1]==15:
            print("DOWN")
        else:
            if nums[-1]-nums[-2]>0:
                print("UP")
            else:
                print("DOWN")
upanddown(nums)