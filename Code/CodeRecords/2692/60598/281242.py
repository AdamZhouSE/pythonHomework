nums = list(map(int, input()[1:-1].split(",")))
day = int(input())
l = 0  # 最小
h = 0  # 最大
for i in range(len(nums)):
    h += nums[i]
    l = max(l, nums[i])


def check(num):
    result = 1
    temp = 0
    for i in range(len(nums)):
        if temp > num:
            result += 1
            temp = 0
            continue
        temp += nums[i]
        if temp > num:
            result += 1
            temp = nums[i]
    return result <= day


while l < h:
    mid = (l + h) // 2
    if check(mid):
        h = mid
    else:
        l = mid +1
print(l)
