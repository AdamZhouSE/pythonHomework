def sort(nums):
    for i in range(1,len(nums)):
        L = 0
        R = i - 1
        M = (L + R)//2
        p = M
        while True:
            middle = nums[M]
            num = nums[i]
            if middle < num:
                L = M + 1
                M = (L + R)//2
            elif middle > num:
                R = M - 1
                M = (L + R) // 2
            else:
                p = M
                break
            if R < L:
                p = L
                break
        nums.insert(p,nums.pop(i))
    return nums

num_tests = int(input())

for i in range(num_tests):
    amount = int(input())
    nums = [int(n) for n in input().split(' ')]
    nums = sort(nums)
    for i in range(len(nums)-1):
        print(str(nums[i])+' ',end='')
    print(nums[-1])