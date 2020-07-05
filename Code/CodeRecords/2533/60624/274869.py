def func29():
    nums = list(map(int, input()[1:-1].split(",")))
    i = 0
    for j in range(len(nums)):
        if nums[j] % 2 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    print(nums)
    return

func29()