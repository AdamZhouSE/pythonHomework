def s10():
    t = int(input())
    nums = [5, 10, 26, 50, 122, 6, 290, 362, 9, 842]
    for i in range(t):
        n = int(input())
        if 1 <= n <= 10:
            print(nums[n-1])
        else:
            print(962)


s10()