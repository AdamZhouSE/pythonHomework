S = input()
N = len(S)
nums = [x for x in range(N + 1)]
left = 0
right = N
res = []
for i in range(0, N):
    if S[i] == 'D':
        res.append(nums[right])
        right -= 1
    else:
        res.append(nums[left])
        left += 1
res.append(nums[left])
print(res)