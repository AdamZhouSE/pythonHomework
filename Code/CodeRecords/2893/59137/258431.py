def s9():
    nums = list(eval(input()))
    for i in range(len(nums)):
        x = nums[i]
        if nums.count(x) == 1:
            print(x)
            return


s9()