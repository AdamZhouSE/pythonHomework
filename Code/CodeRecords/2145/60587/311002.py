T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = input().split(' ')
    heights = [int(nums[i]) for i in range(len(nums))]

    res = 0
    for i in range(n):
        left_i = i
        right_i = i
        while left_i >= 0 and heights[left_i] >= heights[i]:
            left_i -= 1
        while right_i < n and heights[right_i] >= heights[i]:
            right_i += 1
        res = max(res, (right_i - left_i - 1) * heights[i])
    print(res)
