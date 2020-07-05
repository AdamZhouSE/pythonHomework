def s24():
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(input().split())
        for j in range(n):
            nums[j] = int(nums[j])
        nums = sorted(nums)

        if n % 2 == 1:
            print(int(nums[n // 2]))
        else:
            print(int((nums[n // 2] + nums[n // 2 - 1]) // 2))


s24()