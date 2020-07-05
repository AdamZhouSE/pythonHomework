num_test = int(input())
ans = []
for i in range(0, num_test):
    n = int(input())
    nums = [int(x) for x in  input().split()]
    k = int(input())
    nums.sort()
    ans.append(nums[k-1])
for i in ans:
    print(i)
