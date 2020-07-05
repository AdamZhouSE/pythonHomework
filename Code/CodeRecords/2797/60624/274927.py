def func37():
    n = int(input())
    nums = list(map(int, input().split(" ")))
    if nums[n-1] == 15:
        print("DOWN")
    elif nums[n-1] == 0:
        print("UP")
    elif n <= 1:
        print(-1)
    else:
        if nums[n-1] < nums[n-2]:
            if nums[n-1] == 0:
                print("UP")
            else:
                print("DOWN")
        else:
            if nums[n-1] == 15:
                print("DOWN")
            else:
                print("UP")
    return
func37()