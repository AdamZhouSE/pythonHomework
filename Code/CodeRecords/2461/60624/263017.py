def func7():
    nums = list(map(int, input().split(",")))
    low = 0
    high = len(nums)-1
    while low < high:
        mid = (low+high)//2
        if nums[mid] > nums[high]:
            low = mid+1
        elif nums[mid] < nums[high]:
            high = mid
        else:
            high -= 1
    print(nums[low])
    return
func7()