n = int(input())
nums = sorted(list(map(int, input().split(' '))))
if n % 2 == 1:
    s = sum(nums[::2])
    d = sum(nums[1::2])
else:
    s = sum(nums[1::2])
    d = sum(nums[::2])
print(s, d)
