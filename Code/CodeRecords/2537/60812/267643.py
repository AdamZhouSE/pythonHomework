nums = sorted([int(i) for i in input()[1:-1].split(',')], reverse=True)
k = int(input())
print(nums[k-1])