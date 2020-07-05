num_test = int(input())
ans = []
for i in range(0, num_test):
    n = int(input())
    nums = [int(x) for x in input().split()]
    for j in range(0, len(nums)):
        try:
            ind = nums.index(nums[j], j+1)
            ans.append(j+1)
            break
        except Exception:
            pass
        if j == len(nums)-1:
            ans.append(-1)
for i in ans:
    print(i)
