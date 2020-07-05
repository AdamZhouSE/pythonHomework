n = int(input())
nums = [int(i) for i in input().split()]
count = 0
# 将数组归到[1, n]中
for i in range(n):
    if nums[i] <= 0:
        count += 1 - nums[i]
        nums[i] = 1
    elif nums[i] > n:
        count += nums[i] - n
        nums[i] = n
# 将数组归到p排列, 只需对每一个1-n, 选一个离它最近或比它小的到其即可
for i in range(1, n+1):
    if nums.__contains__(i):
        pass
    else:
        near_or_small = n
        for j in nums:
            if j < i and nums.count(j) > 1:
                near_or_small = j
                break
            elif i < j < near_or_small:
                near_or_small = j
            else:
                pass
        count += abs(i - near_or_small)
        nums[nums.index(near_or_small)] = i
print(count)
