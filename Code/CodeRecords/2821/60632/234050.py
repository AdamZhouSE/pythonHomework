n = int(input())
nums = list(map(int, input().split(' ')))
s, d = 0, 0
for i in range(n):
    m = max(nums[0], nums[-1])
    if i % 2 == 0:
        s = s + m
        nums.remove(m)
    else:
        d = d + m
        nums.remove(m)
print(s, d)
