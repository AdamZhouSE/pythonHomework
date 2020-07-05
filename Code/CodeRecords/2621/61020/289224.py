import itertools


def sum_of_list(the_list, left_index, right_index):
    # 和其他的一样，right_index不包含，left_index包含
    result = 0
    for num in the_list[left_index:right_index]:
        result += num
    return result


def stripped_list_of(the_list):
    if (the_list[0] > 0) and (the_list[-1] > 0):
        return the_list

    if not (the_list[0] > 0):
        return stripped_list_of(the_list[1:])

    if not (the_list[-1] > 0):
        return stripped_list_of(the_list[0:-1])


def max_sum_of(the_list):
    stripped_list = stripped_list_of(the_list)
    needed_indexes_of_nums = [0]
    for i in range(len(stripped_list)):
        if stripped_list[i] < 0:
            needed_indexes_of_nums.append(i)

    needed_indexes_of_nums.append(len(stripped_list))
    comb_list_of_indexes = list(itertools.combinations(needed_indexes_of_nums, 2))
    sum_list = []
    for comb in comb_list_of_indexes:
        left_index = min(comb)
        right_index = max(comb)
        sum_list.append(sum_of_list(stripped_list, left_index, right_index))

    return max(sum_list)


nums = input().split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])

print(max_sum_of(nums))

# test


# nums = input().split(',')
# for i in range(len(nums)):
#     nums[i] = int(nums[i])
