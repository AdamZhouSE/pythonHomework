import copy


def div_subset(nums):
    if len(nums) < 2:
        return nums[0]
    nums.sort()
    sub = [[i] for i in nums]
    maxlenl = 0
    maxsub = []
    for i in range(1, len(nums)):
        maxlen = 0
        for j in range(i):
            index = 1
            if nums[i]%nums[j] == 0 and len(sub[j])+1 > maxlen:
                sub[i] = copy.deepcopy(sub[j])
                sub[i].append(nums[i])
                maxlen = len(sub[j])+1
        if len(sub[i]) > maxlenl:
            maxlenl = len(sub[i])
            maxsub = sub[i]
    return maxsub


if __name__ == "__main__":
    nums = [int(i) for i in input().split(',')]
    print(div_subset(nums))
