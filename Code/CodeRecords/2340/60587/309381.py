T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = input().split(' ')
    height = [int(nums[i]) for i in range(len(nums))]
    ans = 0
    for i in range(len(height)):
        max_left, max_right = 0, 0
        # 寻找 max_left
        for j in range(0, i):
            max_left = max(max_left, height[j])
        # 寻找 max_right
        for j in range(i, len(height)):
            max_right = max(max_right, height[j])
        if min(max_left, max_right) > height[i]:
            ans += min(max_left, max_right) - height[i]
    print(ans)
