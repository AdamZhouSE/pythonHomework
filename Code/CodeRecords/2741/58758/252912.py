inp = input()
nums = [int(x) for x in inp[1: len(inp)-1].split(',')]
ans = 1
for i in range(0, len(nums)-ans):
    length = 1
    j = i+1
    while j < len(nums) and nums[j] > nums[j-1]:
        j += 1
        length += 1
    if length > ans:
        ans = length
    i = j-1
print(ans)
