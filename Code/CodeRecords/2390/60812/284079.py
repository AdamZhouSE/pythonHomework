def swap(nums, s1, e1, s2, e2):
    nums[s1:e1], nums[s2:e2] = nums[s2:e2], nums[s1:e1]


def judge(nums, bit):
    global length
    start = fra = 0
    long = bit << 1
    incompatible = []
    while start < length:
        if nums[start+bit-1]+1 != nums[start+bit]:
            incompatible.append(start)
        start += long
    templen = len(incompatible)
    if templen <= 2:
        if templen == 2:
            start, end = incompatible
            # 交换2，3段
            if nums[start + bit - 1] + 1 == nums[end] and nums[start + long - 1] + 1 == nums[end + bit]:
                if long == length:
                    return 1
                swap(nums, start + bit, start + long, end, end + bit)
                temp = judge(nums, long)
                if temp != 0:
                    fra = 1 + temp
                swap(nums, start + bit, start + long, end, end + bit)
            # 交换2，4段或者交换1，3段
            elif nums[start + bit - 1] + 1 == nums[end + bit] and nums[end + bit -1] + 1 == nums[start + bit]:
                # 交换1，3段
                if long == length:
                    return 1
                swap(nums, start, start + bit, end, end + bit)
                temp = judge(nums, long)
                if temp != 0:
                    fra = 1 + temp
                    swap(nums, start, start + bit, end, end + bit)
                    # 得到结果可以返回了，不用考虑交换2，4段的情况，直接还原
                if fra == 0:
                    # 未得到结果，考虑交换2，4段。在1，3段被交换的前提下3 2 1 4 -> 1 4 3 2
                    swap(nums, start, start + long, end, end + long)
                    temp = judge(nums, long)
                    if temp != 0:
                        fra = 1 + temp
                    swap(nums, start + bit, start + long, end + bit, end + long)
            # 交换1，4段
            elif nums[end + long - 1] + 1 == nums[start + bit] and nums[end + bit - 1] + 1 == nums[start]:
                if long == length:
                    return 1
                swap(nums, start, start + bit, end + bit, end + long)
                temp = judge(nums, long)
                if temp != 0:
                    fra = 1 + temp
                swap(nums, start, start + bit, end + bit, end + long)
        elif templen == 1:
            start = incompatible[0]
            if nums[start + long - 1] + 1 == nums[start]:
                if long == length:
                    return 1
                swap(nums, start, start + bit, start + bit, start + long)
                temp = judge(nums, long)
                if temp != 0:
                    fra = 1+temp
                swap(nums, start, start + bit, start + bit, start + long)
        elif long == length:
            return 1
        else:
            fra = judge(nums, long)
    return fra


from functools import reduce
n = int(input())
nums = [int(i) for i in input().split(' ')]
length = 1 << n
fac = judge(nums, 1)
if fac != 0:
    print(reduce(lambda x, y: x*y, range(1, fac+1)))
else:
    print(0)
