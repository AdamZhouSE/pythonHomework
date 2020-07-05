def func7():
    temp = list(map(int, input().split(" ")))
    n, m = temp[0], temp[1]
    nums = list(map(int, input().split(" ")))
    while m > 0:
        m -= 1
        temp = list(map(int, input().split(" ")))
        op, left, right = temp[0], temp[1], temp[2]
        if op == 0:
            nums = nums[:left-1]+sorted(nums[left-1:right])+nums[right:]
        else:
            nums = nums[:left-1]+sorted(nums[left-1:right],reverse=True)+nums[right:]
    target = int(input())
    print(nums[target-1])
    return
func7()