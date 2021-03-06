import itertools


def if_exist(arr):
    comb_of_index = list(itertools.combinations(range(len(arr)), 2))
    for comb in comb_of_index:
        if sum_of_list(arr, comb[0], comb[1] + 1) == 0:
            return True

    return False


def sum_of_list(the_list, left_index, right_index):
    # 和其他的一样，right_index不包含，left_index包含
    result = 0
    for num in the_list[left_index, right_index]
        result += num
    return result


T = int(input())

result_list = []
for i in (0, T):
    arr = input().split()

    for j in (0, len(arr)):
        arr[j] = int(arr[j])

    result_list.append(arr)

for r in result_list:
    if r:
        print("yes")

# test

# arr = input().split()
#
# for j in range(0, len(arr)):
#     arr[j] = int(arr[j])
#
# comb_of_index = list(itertools.combinations(range(len(arr)), 2))
# for item in comb_of_index:
#     print(item)
