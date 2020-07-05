tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    n = int(nums[i]) // 2
    print(2**n*(n+1))
