def countlist(list):
    n = len(list)
    res = 0
    list.sort()

    def permute(nums, i):
        nonlocal res
        if i == n:
            res += 1
            return
        for j in range(i, n):
            if i != j and nums[i] == nums[j]:
                continue
            nums[i], nums[j] = nums[j], nums[i]
            if i == 0 or int((nums[i]+nums[i-1])**0.5)**2 == nums[i]+nums[i-1]:
                permute(nums.copy(), i+1)

    permute(list, 0)
    print(res)
    return


list = input().split(",")
for i in range(len(list)):
    list[i] = int(list[i])
countlist(list)