import itertools


def all_sublist_of(the_list):
    return list(itertools.combinations(the_list, 2))


def is_dengcha_sublist(the_list, difference):
    if len((the_list) == 1):
        return True

    else:
        return is_dengcha_sublist(the_list[1:]) and (the_list[1] - the_list[0] == difference)


arr = input().split(',')
n = int(input())

for i in range(len(arr)):
    arr[i] = int(arr[i])

lens_of_the_sublist = []
for l in all_sublist_of(arr):
    if is_dengcha_sublist(l):
        lens_of_the_sublist.append(len(l))

print(max(lens_of_the_sublist))
