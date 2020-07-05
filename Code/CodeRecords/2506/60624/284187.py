def func12():
    nums = list(map(int, input().split(",")))
    ans = 0
    for i in range(0, len(nums)-1):
        temp = 1
        cur = nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] > cur:
                cur = nums[j]
                temp += 1
        if temp > ans:
            ans = temp
    print(ans)
    return
func12()