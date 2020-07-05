length = int(input())
nums = list(map(int, input().split(" ")))
if length == 1:
    if nums[0] == 15:
        print("DOWN")
    elif nums[0] == 0:
        print("UP")
    else:
        print(-1)
else:
    if nums[-1] == 15:
        print("DOWN")
    elif nums[-1] == 0:
        print("UP")
    else:
        if nums[-1] > nums[-2]:
            print("UP")
        else:
            print("DOWN")

