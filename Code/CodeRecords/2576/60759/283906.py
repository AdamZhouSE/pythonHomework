from math import ceil


def get_nearest(add_sum, nums):
    if len(nums) == 0:
        return max(lst)
    average = add_sum / len(nums)
    while min(nums) <= average:
        min_num = nums.pop(0)
        return get_nearest(add_sum - min_num, nums)
    else:
        down, up = int(average), ceil(add_sum / len(nums))
        if average - down <= up - average:
            return down
        else:
            return up


lst = sorted(list(map(int, input().split(','))))
target = int(input())
print(get_nearest(target, lst.copy()))
