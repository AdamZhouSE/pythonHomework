import itertools


def is_continuous(nums):
    lst = list(nums)
    lst.sort()

    if len(nums) == 1:
        return True

    if len(nums) >= 2:
        return (lst[1] - lst[0] == 1) and is_continuous(lst[1:])

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
for k in range(len(nums)):
    nums[k] = int(nums[k])

print(length_of_the_sub_seq(nums))
# [100, 4, 200, 1, 3, 2]
