n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

for i in range(m):
    rev, start, end = [int(x) for x in input().split()]
    nums[start:end] = sorted(nums[start:end], reverse=rev)
    # print(nums)
q = eval(input())
print(nums[q-1])