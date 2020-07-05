n = int(input())
lst = list(map(int, input().split(' ')))
nums_s = set(lst)
if len(nums_s) <= 2:
    diff = max(lst) - min(lst)
    if (diff / 2) % 1 == 0:
        print(diff // 2)
    else:
        print(diff)
elif len(nums_s) > 3:
    print(-1)
else:
    nums = sorted(list(nums_s))
    if nums[1] - nums[0] == nums[2] - nums[1]:
        print(nums[2] - nums[1])
    else:
        print(-1)
