inp = input()
nums = [int(x) for x in inp[1: len(inp)-1].split(',')]
lower = int(input())
upper = int(input())
ans = 0
for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        if lower <= sum(nums[i: j+1]) <= upper:
            ans += 1
print(ans)
