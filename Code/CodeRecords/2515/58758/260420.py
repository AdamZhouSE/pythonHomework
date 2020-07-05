nums = [int(x) for x in input().split(',')]
m = int(input())
left = max(nums)
right = sum(nums)
mid = (left+right) // 2


def group(bound):
    sum_group = 1
    cnt = 0
    for i in range(0, len(nums)):
        cnt += nums[i]
        if cnt > bound:
            sum_group += 1
            cnt = nums[i]
    return sum_group


while left < right:
    if group(mid) > m:
        left = mid+1
        mid = (left+right) // 2
    elif group(mid) < m:
        right = mid
        mid = (left+right) // 2
    else:
        break
while True:
    mid -= 1
    if group(mid) != m:
        mid += 1
        break
print(mid)
