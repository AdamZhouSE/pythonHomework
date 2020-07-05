import itertools


def is_ascent(nums):
    if len(nums) == 1:
        return True
    if len(nums) > 1:
        return (nums[0] < nums[1]) and is_ascent(nums[1:])


def asc_length_of(nums):
    lengths = []

    combs_of_indexes = list(itertools.combinations(range(0, len(nums)), 2))

    for comb in combs_of_indexes:
        if is_ascent(nums[comb[0], comb[1] + 1]):
            lengths.append(len(comb[1] + 1 - comb[0]))

    # TODO: 遍历下标组合、添加到lengths，用max返回
    return max(lengths)


nums = input()[1:-1].split(',')
for i in range(0, len(nums)):
    nums[i] = int(nums[i])

print(asc_length_of(nums))
