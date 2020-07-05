ns, s = map(int, input().split(' '))
nums = []
for n in range(ns):
    nums.append(int(input()))
for i in range(len(nums) - 1):
    ans = 0
    for j in range(i + 2, len(nums) + 1, 2):
        idx = (i + j) // 2
        if sum(nums[i:idx]) <= s and sum(nums[idx:j]) <= s:
            ans = j - i
    print(ans)
print(0)
