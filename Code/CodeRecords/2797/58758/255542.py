days = int(input())
nums = [int(x) for x in input().split()]
if days == 1:
    if nums[0] == 0:
        print('UP')
    elif nums[0] == 15:
        print('DOWN')
    else:
        print(-1)
else:
    if nums[days-1] == 15:
        print('DOWN')
    elif nums[days-1] == 0:
        print('UP')
    elif nums[days-1] > nums[days-2]:
        print('UP')
    else:
        print('DOWN')
