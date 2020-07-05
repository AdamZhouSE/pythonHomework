def func16():
    nums = list(map(int, input()[1:-1].split(",")))
    if len(nums) == 0:
        print(0)
    else:
        length, max_length = 1, 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                length += 1
                if length > max_length:
                    max_length = length
            else:
                length = 1
        print(max_length)
    return
func16()
