n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))
for i in range(m):
    cmd = input().split()
    if cmd[0] == 'Q':
        l, r, k = list(map(int, [cmd[1], cmd[2] ,cmd[3]]))
        print(sorted(nums[l - 1:r])[k - 1])
    elif cmd[0] == 'C':
        ax, y = list(map(int, [cmd[1], cmd[2]]))
        if ax in nums:
            nums[nums.index(ax)] = y
