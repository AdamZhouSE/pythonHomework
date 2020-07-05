k, m = input().split()
k, m = int(k), int(m)
nums = [1]
idx1, idx2 = 0, 0
i1, i2 = 2 * nums[idx1] + 1, 4 * nums[idx2] + 5
while len(nums) < k:
    add_i = min(i1, i2)
    nums.append(add_i)
    if i1 < i2:
        idx1 += 1
        i1 = 2 * nums[idx1] + 1
    else:
        idx2 += 1
        i2 = 4 * nums[idx2] + 5
        if i1 == i2:
            idx1 += 1
            i1 = 2 * nums[idx1] + 1

before = ''.join(map(str, nums))
nums = list(map(int, list(before)))
ans = ''
b_idx, a_idx = 0, m
while len(ans) < len(nums) - m:
    max_n = max(nums[b_idx:a_idx + 1])
    ans += str(max_n)
    # index找到的是满足条件的第一个，需要限制其下标范围
    b_idx += nums[b_idx:a_idx + 1].index(max_n) + 1
    a_idx += 1
print(before)
print(ans, end='')
