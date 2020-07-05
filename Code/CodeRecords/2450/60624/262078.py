def func3():
    temp = input()
    nums = list(map(int, temp.split(",")))
    target = int(input())
    res = [-1,-1]
    if len(nums) == 0:
        print(res)
    res = searchRange(nums, target)
    print(res)
    return


def searchRange(nums: list, target: int) -> list:
    low = 0
    high = len(nums)-1
    ans = [-1,-1]
    if len(nums) < 1:
        return ans
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            before = mid-1
            while before >= 0:
                if nums[before] != target:
                    break
                before -= 1
            ans[0] = before+1
            after = mid+1
            while after <= len(nums)-1:
                if nums[after] != target:
                    break
                after += 1
            ans[1] = after-1
            break
        elif nums[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return ans
func3()