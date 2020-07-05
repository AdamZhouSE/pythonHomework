def func7():
    nums = list(map(int, input()[1:-1].split(",")))
    counts = []
    for i in range(0,len(nums)-1):
        temp = 0
        for num in nums[i+1:]:
            if num < nums[i]:
                temp += 1
        counts.append(temp)
    counts.append(0)
    print(counts)
    return
func7()