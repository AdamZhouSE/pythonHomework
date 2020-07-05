def idx_of_min(nums):
    idx = 0
    mini = nums[0]
    for i in range(len(nums)):
        if nums[i] < mini:
            mini = nums[i]
            idx = i
    return idx


n = int(input())
height = [int(x) for x in input().split(' ')]
height.insert(0,0)
result = []

for idx in range(1,len(height)):
    P = idx_of_min(height[idx:])+idx
    result.append(P)
    tmp = height[idx:P+1]
    height[idx:P+1] = reversed(tmp)

for i in result:
    print(str(i) + ' ',end = '')


