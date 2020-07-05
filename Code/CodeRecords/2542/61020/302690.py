import itertools


def is_continuous(nums):
    lst = list(nums)
    lst.sort()

    if len(nums) == 1:
        return True

    if len(nums) >= 2:
        return (nums[1] - nums[0] == 1) and is_continuous(nums[1:])

    pass


def length_of_the_sub_seq(nums):
    lengths = set()
    for i in range(len(nums), 0, -1):
        combs_of_nums = list(itertools.combinations(nums, i))
        for comb in combs_of_nums:
            if is_continuous(comb):
                lengths.add(i)
                break

    return max(lengths)


nums = input()[1:-1].split(', ')

print(length_of_the_sub_seq(nums))