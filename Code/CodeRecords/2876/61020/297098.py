import itertools
import copy


def indexes_of(a_list_, ele):
    result = []
    for j in range(len(a_list_)):
        if a_list_[j] == ele:
            result.append(j)

    return result

def is_done(a_list):
    if len(a_list) <= 2:
        return True

    if len(a_list) == 3:
        if a_list != ['1', '0', '1']:
            return True

        return False

    if len(a_list) > 3:
        return is_done(a_list[0:3]) and is_done(a_list[1:])


def min_switch(a_list):
    indexes_of_1 = indexes_of(a_list, '1')
    if is_done(a_list):
        return 0

    for i in range(1, len(indexes_of_1)):
        coms = list(itertools.combinations(indexes_of_1, 1))
        for indexes in coms:
            seq_to_be_change = copy.copy(a_list)
            for index in indexes:
                seq_to_be_change[index] = 0
                if is_done(seq_to_be_change):
                    return i


trash = input()
nums = input().split()
print(min_switch(nums))

# test1
# import copy
#
# a = ['0', '1', '2']
# b = copy.copy(a)
#
# print(a == b)
# print(a is b)
#
# b[1] = '4'
# print(a)
# print(b)


# test2
# import copy
#
# a = ['0', '1', '2']
# b = copy.deepcopy(a)
# print(a == b)
# print(a is b)
