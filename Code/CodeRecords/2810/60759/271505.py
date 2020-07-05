nums = list(map(int, list(input())))
ans = []
while nums.count(0) < len(nums):
    item_s = ''
    for i in range(len(nums)):
        item_s += '1' if nums[i] >= 1 else '0'
    while item_s.startswith('0'):
        item_s = item_s[1:]
    ans.append(item_s)
    nums = list(map(lambda x: max(x - 1, 0), nums))
print(len(ans))
print(' '.join(ans))
