n = eval(input())
nums = [0]
ans = 0
energy = [0] * (n + 1)
nums.extend([int(x) for x in input().split()])
energy[0] = nums[0] - nums[1]
for i in range(n - 1):
    if energy[i] < 0:
        ans += -energy[i]
        energy[i] = 0
    energy[i + 1] = energy[i] + nums[i + 1] - nums[i + 2]
if energy[n] < 0:
    ans += -energy[n]
    energy[n] = 0
print(ans)