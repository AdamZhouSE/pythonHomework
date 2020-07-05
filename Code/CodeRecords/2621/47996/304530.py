string = input()
nums = string.split(",")
length = len(nums)
n = int(nums[0])
ans = n
s = n
m = 0
for i in range(1, length):
    if s < m:
        m = s
    s += int(nums[i])
    if s - m > ans:
        ans = s - m
print(ans)
