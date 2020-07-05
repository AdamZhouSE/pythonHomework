def s17():
    t = int(input())
    for x in range(t):
        n = int(input())
        nums = list(input().split())

        for i in range(n):
            nums[i] = int(nums[i]) % 3

        count = nums.count(0)
        x = nums.count(1)
        y = nums.count(2)
        z = min(x, y)
        count = count + z
        x = x - z
        y = y - z

        if x != 0:
            count = count + x // 3
        if y != 0:
            count = count + y // 3

        print(count)


s17()