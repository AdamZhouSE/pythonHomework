T = eval(input())
for i in range(T):
    N = eval(input())
    nums = [int(x) for x in input().split()]
    if N <= 2:
        print(0)
        continue
    # arr = np.array(nums)

    curHeightL = nums[0]
    curHeightR = nums[N - 1]
    leftIdx = 0
    rightIdx = N - 1

    while leftIdx < N - 1 and nums[leftIdx + 1] > curHeightL:
        leftIdx += 1
        curHeightL = nums[leftIdx]
    while rightIdx > 0 and nums[rightIdx - 1] > curHeightR:
        rightIdx += 1
        curHeightR = nums[rightIdx]
    res = 0
    while leftIdx < rightIdx:
        if curHeightL <= curHeightR:
            while leftIdx != rightIdx:
                if nums[leftIdx] > curHeightL:
                    curHeightL = nums[leftIdx]
                    break
                else:
                    res += curHeightL - nums[leftIdx]
                leftIdx += 1
        else:
            while leftIdx != rightIdx:
                if nums[rightIdx] > curHeightR:
                    curHeightR = nums[rightIdx]
                    break
                else:
                    res += curHeightR - nums[rightIdx]
                rightIdx -= 1
    print(res)