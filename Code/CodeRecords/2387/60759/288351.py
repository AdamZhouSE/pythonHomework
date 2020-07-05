n, ms = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
for m in range(ms):
    op, l, r = map(int, input().split(' '))
    temp = sorted(nums[l - 1:r], reverse=op)
    nums = nums[:l - 1] + temp + nums[r:]
print(nums[int(input()) - 1])
