s = input()
nums = []
for i in range(0, 10):
    nums.append(0)
for i in range(0, len(s)):
    if s[i] == 'z':
        nums[0] += 1
    elif s[i] == 'o':
        nums[1] += 1
    elif s[i] == 'w':
        nums[2] += 1
    elif s[i] == 'h':
        nums[3] += 1
    elif s[i] == 'u':
        nums[4] += 1
    elif s[i] == 'f':
        nums[5] += 1
    elif s[i] == 'x':
        nums[6] += 1
    elif s[i] == 'v':
        nums[7] += 1
    elif s[i] == 'g':
        nums[8] += 1
    elif s[i] == 'i':
        nums[9] += 1
    else:
        continue
nums[1] -= (nums[0]+nums[2]+nums[4])
nums[3] -= nums[8]
nums[5] -= nums[4]
nums[7] -= nums[5]
nums[9] -= (nums[5]+nums[6]+nums[8])
ans = ''
for i in range(0, 10):
    if nums[i] != 0:
        ans += str(i)
print(ans)
