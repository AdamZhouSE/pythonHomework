def func12():
    def dfs(nums, begin, n, target):
        if n == 0:
            return target == 0
        if target < n * nums[begin]:
            return False
        for i in range(begin, len(nums)-n+1):
            if i > begin and nums[i]==nums[i-1]:
                continue
            if dfs(nums, i+1, n-1, target-nums[i]):
                return True
    nums = list(map(int, input().split(",")))
    Sum = sum(nums)
    n = len(nums)
    nums.sort()
    flag = False
    for i in range(1, len(nums)//2+1):
        if Sum*i%n==0 and Sum*i/n<float(Sum) and dfs(nums, 0, i, Sum*i/n):
            flag = True
    print(flag)
    return
func12()