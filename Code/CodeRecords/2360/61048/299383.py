import math
def numop35():
    str_in=input().split(',')
    A=[int(x) for x in str_in]
    n = len(A)
    res=0
    set=[]

    def permute(nums, i):
        nonlocal res
        if i == n:
            if(nums not in set):
                set.append(list(nums))
                res += 1
            return
        for k in range(i, n):
            if i != k and nums[i] == nums[k]:
                continue
            nums[i], nums[k] = nums[k], nums[i]
            if i == 0 or int(math.sqrt(nums[i] + nums[i - 1]) ) ** 2 == (nums[i] + nums[i - 1]):
                permute(nums, i + 1)

    A.sort()
    permute(A, 0)
    print(res)
    return 0


numop35()