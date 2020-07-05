n, m = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
nums.reverse()
print(n - nums.index(max(nums)))