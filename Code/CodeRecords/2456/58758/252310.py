inp = input()
nums = [int(x) for x in inp[1: len(inp)-1].split(',')]
ans = []
for i in range(0, len(nums)):
    count = 0
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            count += 1
    ans.append(count)
print(ans)
