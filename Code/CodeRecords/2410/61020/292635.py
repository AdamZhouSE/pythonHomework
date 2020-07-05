import itertools


def all_sublist_of(the_list):
    result = []
    for i in range(1, len(the_list)):
        result.append(itertools.combinations(the_list, i))

    return result


def is_dengcha_sublist(the_list, difference):
    if len(the_list) == 1:
        return True

    else:
        return is_dengcha_sublist(the_list[1:], difference) and (the_list[1] - the_list[0] == difference)


arr = input()[1:-1].split(',')
n = int(input())

for i in range(len(arr)):
    arr[i] = int(arr[i])

lens_of_the_sublist = []
for l in all_sublist_of(arr):
    for j in l:
        if is_dengcha_sublist(j, n):
            lens_of_the_sublist.append(len(j))

print(max(lens_of_the_sublist))
