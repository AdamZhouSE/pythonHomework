def s26():
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(input().split())
        for j in range(n):
            nums[j] = int(nums[j])
        nums = sorted(nums)

        a = nums[0]
        b = nums[-1]
        for x in range(b, a*b+1):
            if x % a == 0 and x % b == 0:
                print(x)
                break


s26()