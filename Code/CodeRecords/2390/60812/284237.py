def judge(nums, bit):
    global length
    start = 0
    fra = []
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
            if nums[start + bit - 1] + 1 == nums[end] and nums[start + long - 1] + 1 == nums[end + bit]:
                if long == length:
                    return [1]
                swap(nums, start + bit, start + long, end, end + bit)
                temp = judge(nums, long)
                if temp:
                    for i in range(len(temp)):
                        temp[i] += 1
                    fra = temp
                swap(nums, start + bit, start + long, end, end + bit)
            elif nums[start + bit - 1] + 1 == nums[end + bit] and nums[end + bit -1] + 1 == nums[start + bit]:
                if long == length:
                    return 1
                swap(nums, start, start + bit, end, end + bit)
                temp = judge(nums, long)
                if temp:
                    for i in range(len(temp)):
                        temp[i] += 1
                    fra = temp
                swap(nums, start, start + long, end, end + long)
                temp = judge(nums, long)
                if temp:
                    for i in range(len(temp)):
                        fra.append(temp[i] + 1)
                swap(nums, start + bit, start + long, end + bit, end + long)
            elif nums[end + long - 1] + 1 == nums[start + bit] and nums[end + bit - 1] + 1 == nums[start]:
                if long == length:
                    return [1]
                swap(nums, start, start + bit, end + bit, end + long)
                temp = judge(nums, long)
                if temp:
                    for i in range(len(temp)):
                        temp[i] += 1
                    fra = temp
                swap(nums, start, start + bit, end + bit, end + long)
        elif templen == 1:
            start = incompatible[0]
            if nums[start + long - 1] + 1 == nums[start]:
                if long == length:
                    return [1]
                swap(nums, start, start + bit, start + bit, start + long)
                temp = judge(nums, long)
                if temp:
                    for i in range(len(temp)):
                        temp[i] += 1
                    fra = temp
                swap(nums, start, start + bit, start + bit, start + long)
        elif long == length:
            return [0]
        else:
            fra = judge(nums, long)
    return fra


def swap(nums, s1, e1, s2, e2):
    nums[s1:e1], nums[s2:e2] = nums[s2:e2], nums[s1:e1]


from functools import reduce
n = int(input())
nums = [int(i) for i in input().split(' ')]
length = 1 << n
fac = judge(nums, 1)
if fac:
    sum = 0
    for i in fac:
        sum += reduce(lambda x, y: x*y, range(1, i+1))
    print(sum)
else:
    print(0)